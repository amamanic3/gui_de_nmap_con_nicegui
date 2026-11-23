import ipaddress
from pydantic import BaseModel, Field, field_validator

class ScanRequest(BaseModel):
    target: str
    profile: str = "ping"
    ports: str | None = None
    authorized: bool = False

    @field_validator("target")
    @classmethod
    def validate_target(cls, value: str) -> str:
        value = value.strip()
        if not value or any(c in value for c in "\r\n;|&`$><"):
            raise ValueError("Enter a valid IP address, hostname, or CIDR range.")
        if "/" in value:
            ipaddress.ip_network(value, strict=False)
        return value

    @field_validator("ports")
    @classmethod
    def validate_ports(cls, value: str | None) -> str | None:
        if value is None or not value.strip():
            return None
        if not all(c in "0123456789,-" for c in value):
            raise ValueError("Ports must use a numeric list or range, such as 22,80,443 or 1-1024.")
        for part in value.split(","):
            bounds = part.split("-")
            if len(bounds) > 2 or any(not b for b in bounds):
                raise ValueError("Invalid port list or range.")
            nums = [int(b) for b in bounds]
            if any(n < 1 or n > 65535 for n in nums) or (len(nums) == 2 and nums[0] > nums[1]):
                raise ValueError("Ports must be between 1 and 65535, with ranges in ascending order.")
        return value.strip()
