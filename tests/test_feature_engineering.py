import pandas as pd
from src.feature_engineering import create_rfm

def test_create_rfm():
    df = pd.DataFrame({
        'InvoiceNo': ['1','2','3','4'],
        'CustomerID': [1,1,2,2],
        'Quantity': [1,1,1,1],
        'UnitPrice': [10,10,10,10],
        'InvoiceDate': pd.to_datetime(['2020-01-01','2020-01-10','2020-01-05','2020-01-15']),
        'TotalAmount': [10,10,10,10],
        'StockCode': ['A','A','B','B'],
        'Description': ['x','x','y','y'],
        'Country': ['UK','UK','UK','UK']
    })
    rfm = create_rfm(df)
    assert set(['CustomerID','Recency','Frequency','Monetary']).issubset(rfm.columns)
    assert len(rfm) == 2
