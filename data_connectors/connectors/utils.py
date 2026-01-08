import yaml
from typing import Dict

def load_yaml_config(path: str) -> Dict:
    """Load configuration from a YAML file"""
    import os
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r") as f:
        return yaml.safe_load(f)
