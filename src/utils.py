import random
 
import numpy as np
import yaml
 
 
def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)
 
 
def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
