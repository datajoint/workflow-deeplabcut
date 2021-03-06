import datajoint as dj


def get_dlc_root_data_dir():
    dlc_root_dirs = dj.config.get("custom", {}).get("dlc_root_data_dir")
    if not dlc_root_dirs:
        return None
    elif not isinstance(dlc_root_dirs, list):
        return list(dlc_root_dirs)
    else:
        return dlc_root_dirs


def get_dlc_processed_data_dir() -> str:
    """Returns session_dir relative to custom 'dlc_output_dir' root"""
    from pathlib import Path

    dlc_output_dir = dj.config.get("custom", {}).get("dlc_output_dir")
    if dlc_output_dir:
        return Path(dlc_output_dir)
    else:
        return get_dlc_root_data_dir()[0]
