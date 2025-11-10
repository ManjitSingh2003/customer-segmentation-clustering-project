from typing import Tuple, List
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import silhouette_score
import numpy as np
import joblib

FEATURES_DEFAULT = ['Recency', 'Frequency', 'Monetary']

def kmeans_pipeline(n_clusters: int = 4, random_state: int = 42) -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=n_clusters, n_init='auto', random_state=random_state))
    ])

def fit_predict_kmeans(df: pd.DataFrame, feature_cols: List[str] = None, n_clusters: int = 4) -> Tuple[pd.DataFrame, Pipeline, float, float]:
    """Fit KMeans on selected features and attach labels. Returns (df_with_labels, pipeline, inertia, silhouette)."""
    feature_cols = feature_cols or FEATURES_DEFAULT
    X = df[feature_cols].values
    pipe = kmeans_pipeline(n_clusters=n_clusters)
    labels = pipe.fit_predict(X)
    inertia = pipe.named_steps['kmeans'].inertia_
    # Compute silhouette on scaled features
    X_scaled = pipe.named_steps['scaler'].transform(X)
    sil = silhouette_score(X_scaled, labels) if len(np.unique(labels)) > 1 else float('nan')
    out = df.copy()
    out['Cluster'] = labels
    return out, pipe, float(inertia), float(sil)

def save_model(pipe: Pipeline, path: str) -> None:
    joblib.dump(pipe, path)

def load_model(path: str) -> Pipeline:
    return joblib.load(path)
