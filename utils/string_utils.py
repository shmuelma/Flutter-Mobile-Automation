import re

def to_snake_case(name: str) -> str:
    """
    ממיר מחרוזות כמו platformName → platform_name
    """
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
