"""Small shared helpers used by more than one module."""

import random
import yaml
import numpy as np


def load_config(path: str = "config.yaml") -> dict:
    """Read and examines the pipeline's config.yaml file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed: int = 42) -> None:
    """Fix the random seed for numpy and Python's random module, so the runs
    are reproducible. Note: individual models still need their own
    random_state passed in separately."""
    random.seed(seed)
    np.random.seed(seed)