from typing import Optional


def safe_convert_to_int(s) -> Optional[int]:
    try:
        result = int(s)
        return result
    except ValueError:
        return None
