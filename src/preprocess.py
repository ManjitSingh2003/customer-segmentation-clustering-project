import pandas as pd

REQUIRED_COLS = [
    'InvoiceNo','StockCode','Description','Quantity','InvoiceDate',
    'UnitPrice','CustomerID','Country'
]

def ensure_columns(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean Online Retail style dataset."""
    df = ensure_columns(df.copy())
    # Basic cleaning
    df = df.dropna(subset=['CustomerID'])
    df['CustomerID'] = df['CustomerID'].astype(int)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] >= 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    # Remove credit notes / cancellations (InvoiceNo starting with 'C')
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    # Compute line total
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    return df
