from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.connection import Base

def now(): return datetime.now(timezone.utc)

class Scan(Base):
    __tablename__ = "scans"
    id: Mapped[int] = mapped_column(primary_key=True)
    target_scope: Mapped[str] = mapped_column(String(255))
    scan_configuration: Mapped[str] = mapped_column(Text, default="{}")
    scan_profile: Mapped[str] = mapped_column(String(60))
    status: Mapped[str] = mapped_column(String(30), default="queued", index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    duration: Mapped[float | None] = mapped_column(Float)
    error_message: Mapped[str | None] = mapped_column(Text)
    hosts: Mapped[list["HostObservation"]] = relationship(back_populates="scan", cascade="all, delete-orphan")

class Host(Base):
    __tablename__ = "hosts"
    id: Mapped[int] = mapped_column(primary_key=True)
    ip_address: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hostname: Mapped[str | None] = mapped_column(String(255))
    mac_address: Mapped[str | None] = mapped_column(String(40), index=True)
    status: Mapped[str] = mapped_column(String(30), default="unknown")
    operating_system: Mapped[str | None] = mapped_column(String(255))
    first_seen: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    last_seen: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    observations: Mapped[list["HostObservation"]] = relationship(back_populates="host")

class HostObservation(Base):
    __tablename__ = "host_observations"
    id: Mapped[int] = mapped_column(primary_key=True)
    host_id: Mapped[int] = mapped_column(ForeignKey("hosts.id", ondelete="CASCADE"), index=True)
    scan_id: Mapped[int] = mapped_column(ForeignKey("scans.id", ondelete="CASCADE"), index=True)
    host: Mapped[Host] = relationship(back_populates="observations")
    scan: Mapped[Scan] = relationship(back_populates="hosts")
    ports: Mapped[list["Port"]] = relationship(back_populates="observation", cascade="all, delete-orphan")
    __table_args__ = (UniqueConstraint("host_id", "scan_id"),)

class Port(Base):
    __tablename__ = "ports"
    id: Mapped[int] = mapped_column(primary_key=True)
    observation_id: Mapped[int] = mapped_column(ForeignKey("host_observations.id", ondelete="CASCADE"), index=True)
    port_number: Mapped[int] = mapped_column(Integer)
    protocol: Mapped[str] = mapped_column(String(8))
    state: Mapped[str] = mapped_column(String(30))
    observation: Mapped[HostObservation] = relationship(back_populates="ports")
    service: Mapped["Service | None"] = relationship(back_populates="port", cascade="all, delete-orphan", uselist=False)
    __table_args__ = (UniqueConstraint("observation_id", "port_number", "protocol"),)

class Service(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key=True)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id", ondelete="CASCADE"), unique=True)
    service_name: Mapped[str | None] = mapped_column(String(100))
    product: Mapped[str | None] = mapped_column(String(255))
    version: Mapped[str | None] = mapped_column(String(120))
    extra_information: Mapped[str | None] = mapped_column(Text)
    port: Mapped[Port] = relationship(back_populates="service")

class WhitelistDevice(Base):
    __tablename__ = "whitelist_devices"
    id: Mapped[int] = mapped_column(primary_key=True)
    ip_address: Mapped[str | None] = mapped_column(String(100), index=True)
    mac_address: Mapped[str | None] = mapped_column(String(40), index=True)
    hostname: Mapped[str | None] = mapped_column(String(255), index=True)
    description: Mapped[str | None] = mapped_column(Text)
    owner: Mapped[str | None] = mapped_column(String(255))
    authorization_status: Mapped[str] = mapped_column(String(30), default="authorized")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now, onupdate=now)

class HostGroup(Base):
    __tablename__ = "host_groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    description: Mapped[str | None] = mapped_column(Text)

class HostGroupMember(Base):
    __tablename__ = "host_group_members"
    id: Mapped[int] = mapped_column(primary_key=True)
    host_group_id: Mapped[int] = mapped_column(ForeignKey("host_groups.id", ondelete="CASCADE"))
    host_id: Mapped[int] = mapped_column(ForeignKey("hosts.id", ondelete="CASCADE"))

class ScanComparison(Base):
    __tablename__ = "scan_comparisons"
    id: Mapped[int] = mapped_column(primary_key=True)
    scan_id_1: Mapped[int] = mapped_column(ForeignKey("scans.id"))
    scan_id_2: Mapped[int] = mapped_column(ForeignKey("scans.id"))
    comparison_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=now)
    results: Mapped[str] = mapped_column(Text, default="{}")

class Traceroute(Base):
    __tablename__ = "traceroutes"
    id: Mapped[int] = mapped_column(primary_key=True)
    scan_id: Mapped[int] = mapped_column(ForeignKey("scans.id", ondelete="CASCADE"), index=True)
    host_id: Mapped[int | None] = mapped_column(ForeignKey("hosts.id", ondelete="SET NULL"))
    hop_number: Mapped[int] = mapped_column(Integer)
    hop_address: Mapped[str | None] = mapped_column(String(100))
    latency: Mapped[float | None] = mapped_column(Float)

class NseResult(Base):
    __tablename__ = "nse_results"
    id: Mapped[int] = mapped_column(primary_key=True)
    scan_id: Mapped[int] = mapped_column(ForeignKey("scans.id", ondelete="CASCADE"), index=True)
    host_id: Mapped[int | None] = mapped_column(ForeignKey("hosts.id", ondelete="SET NULL"))
    script_name: Mapped[str] = mapped_column(String(120))
    output: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30), default="completed")
