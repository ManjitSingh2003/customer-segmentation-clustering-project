import pandas as pd
from src.preprocess import clean_data

def test_clean_data_basic():
    df = pd.DataFrame({
        'InvoiceNo': ['10001','C10002','10003'],
        'StockCode': ['A','B','C'],
        'Description': ['x','y','z'],
        'Quantity': [1, -2, 3],
        'InvoiceDate': ['2020-01-01','2020-01-02','2020-01-03'],
        'UnitPrice': [2.0, 3.0, 4.0],
        'CustomerID': [123.0, 456.0, 789.0],
        'Country': ['UK','UK','UK']
    })
    out = clean_data(df)
    # Removes negative quantity, credit notes, keeps only valid rows
    assert len(out) == 2
    assert (out['TotalAmount'] >= 0).all()
