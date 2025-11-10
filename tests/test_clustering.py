import pandas as pd
from src.clustering import fit_predict_kmeans

def test_fit_predict_kmeans_runs():
    rfm = pd.DataFrame({
        'CustomerID': [1,2,3,4,5,6,7,8],
        'Recency': [10,20,30,40,11,21,31,41],
        'Frequency': [5,2,3,1,6,2,4,1],
        'Monetary': [100,50,60,20,110,55,65,25]
    })
    out, pipe, inertia, sil = fit_predict_kmeans(rfm, n_clusters=3)
    assert 'Cluster' in out.columns
    assert len(out['Cluster'].unique()) <= 3
