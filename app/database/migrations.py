"""Schema initialization hook. create_all handles new databases; future revisions belong here."""
def migrate(engine) -> None:
    # Kept as a single entry point so versioned migrations can be added compatibly.
    return None
