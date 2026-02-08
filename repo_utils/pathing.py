from __future__ import annotations

import os
from pathlib import Path
from typing import Optional


def project_root() -> Path:
    # repo_utils/ -> <repo_root>
    return Path(__file__).resolve().parents[1]


def is_kaggle() -> bool:
    return Path("/kaggle").exists() or os.environ.get("KAGGLE_URL_BASE") is not None


def artifacts_dir(name: str = "artifacts") -> Path:
    if is_kaggle():
        p = Path("/kaggle/working") / name
    else:
        p = project_root() / name
    p.mkdir(parents=True, exist_ok=True)
    return p


def resolve_data_path(
    filename: str,
    *,
    local_dir: str = "data/raw",
    kaggle_subdir_hint: Optional[str] = None,
    env_var: str = "DATA_PATH",
) -> Path:
    """Resolve a dataset file path.

    Resolution order:
    1) If env var `DATA_PATH` points to an existing file -> use it.
    2) Local: <repo_root>/<local_dir>/<filename>
    3) Kaggle: /kaggle/input/<kaggle_subdir_hint>/<filename> (if provided)
    4) Kaggle fallback: search /kaggle/input/**/<filename>

    Raises FileNotFoundError with a clear message if not found.
    """
    env_path = os.environ.get(env_var)
    if env_path:
        p = Path(env_path).expanduser()
        if p.exists() and p.is_file():
            return p

    local_path = project_root() / local_dir / filename
    if local_path.exists() and local_path.is_file():
        return local_path

    if is_kaggle():
        if kaggle_subdir_hint:
            hinted = Path("/kaggle/input") / kaggle_subdir_hint / filename
            if hinted.exists() and hinted.is_file():
                return hinted

        for p in Path("/kaggle/input").glob(f"**/{filename}"):
            if p.is_file():
                return p

    raise FileNotFoundError(
        f"Could not find '{filename}'.\n"
        f"- Put it under '{local_dir}/' (local)\n"
        f"- Or set {env_var} to the full file path\n"
        f"- On Kaggle, ensure the dataset is added to the notebook."
    )
