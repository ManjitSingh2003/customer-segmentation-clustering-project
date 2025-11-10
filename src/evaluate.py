from typing import List
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def silhouette_on_features(df: pd.DataFrame, feature_cols: List[str], labels_col: str = 'Cluster') -> float:
    X = df[feature_cols].values
    Xs = StandardScaler().fit_transform(X)
    return float(silhouette_score(Xs, df[labels_col]))

def cluster_profile(df: pd.DataFrame, cluster_col: str = 'Cluster'):
    return df.groupby(cluster_col).agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean',
        }).round(2)

def plot_elbow(inertias, ks):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(7,5))
    plt.plot(ks, inertias, marker='o')
    plt.title('Elbow Method (Inertia vs k)')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.tight_layout()
    plt.show()
