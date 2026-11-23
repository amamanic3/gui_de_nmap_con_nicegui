import platform

def get_platform_info() -> dict[str, str]:
    return {"system": platform.system(), "release": platform.release(), "version": platform.version(), "machine": platform.machine()}
