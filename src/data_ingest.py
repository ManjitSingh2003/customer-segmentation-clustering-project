import pandas as pd
import os
from typing import Union, IO

def load_data(file_path_or_buffer: Union[str, IO]) -> pd.DataFrame:
    """Load dataset from CSV or Excel. Accepts file path or file-like object."""
    if hasattr(file_path_or_buffer, 'read'):
        # file-like (e.g., Streamlit uploader)
        try:
            return pd.read_csv(file_path_or_buffer, encoding='ISO-8859-1')
        except Exception:
            file_path_or_buffer.seek(0)
            return pd.read_excel(file_path_or_buffer)
    else:
        ext = os.path.splitext(str(file_path_or_buffer))[1].lower()
        if ext == '.csv':
            return pd.read_csv(file_path_or_buffer, encoding='ISO-8859-1')
        elif ext in ('.xls', '.xlsx'):
            return pd.read_excel(file_path_or_buffer)
        else:
            raise ValueError(f"Unsupported file format: {ext}")

def save_processed(df: pd.DataFrame, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
