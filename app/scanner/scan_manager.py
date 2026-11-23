import asyncio
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from app.scanner.nmap_engine import NmapEngine

@dataclass
class ScanJob:
    id: str
    request: dict
    status: str = "queued"
    result: list = field(default_factory=list)
    error: str | None = None
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class ScanManager:
    def __init__(self, engine=None, workers=2):
        self.engine = engine or NmapEngine()
        self.pool = ThreadPoolExecutor(max_workers=workers)
        self.jobs = {}
        self.active_targets = set()
    async def submit(self, request: dict) -> ScanJob:
        target = request["target"]
        if target in self.active_targets: raise ValueError("A scan for this target is already running.")
        job = ScanJob(str(uuid.uuid4()), request); self.jobs[job.id] = job; self.active_targets.add(target)
        asyncio.create_task(self._run(job)); return job
    async def _run(self, job):
        job.status = "running"
        try:
            job.result = await asyncio.get_running_loop().run_in_executor(self.pool, self.engine.scan, job.request)
            job.status = "completed"
        except Exception as exc:
            print(type(exc))
            print(exc.args)
            print(exc)
            job.error = str(exc); 
            job.status = "failed"
        finally: self.active_targets.discard(job.request["target"])
    def cancel(self, job_id: str) -> bool:
        job = self.jobs.get(job_id)
        if not job or job.status not in {"queued", "running"}: return False
        job.status = "interrupted"; self.active_targets.discard(job.request["target"]); return True
