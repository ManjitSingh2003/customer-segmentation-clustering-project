import pandas as pd

def create_rfm(df: pd.DataFrame, date_col: str = 'InvoiceDate') -> pd.DataFrame:
    """Create Recency, Frequency, Monetary features per CustomerID."""
    snapshot_date = df[date_col].max() + pd.Timedelta(days=1)
    grouped = df.groupby('CustomerID')
    rfm = grouped.agg({
        date_col: lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalAmount': 'sum'
    }).rename(columns={
        date_col: 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalAmount': 'Monetary'
    }).reset_index()
    return rfm

def add_additional_features(df: pd.DataFrame) -> pd.DataFrame:
    """Optional: mean basket size etc. Requires pre-aggregated or transactional input."""
    # No-op placeholder for extensibility
    return df
