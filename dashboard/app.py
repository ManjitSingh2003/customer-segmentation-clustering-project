import streamlit as st
import pandas as pd
from io import BytesIO

from src.data_ingest import load_data
from src.preprocess import clean_data
from src.feature_engineering import create_rfm
from src.clustering import fit_predict_kmeans
from src.insights import label_segments, segment_recommendations

st.set_page_config(page_title='Customer Segmentation', layout='wide')
st.title('🛍️ Customer Segmentation Dashboard')

st.sidebar.header('Config')
k = st.sidebar.slider('Number of clusters (k)', min_value=2, max_value=10, value=4, step=1)

uploaded = st.file_uploader('Upload Online Retail dataset (CSV or XLSX)', type=['csv','xlsx','xls'])

if uploaded is not None:
    with st.spinner('Loading & cleaning data...'):
        df_raw = load_data(uploaded)
        df = clean_data(df_raw)

    st.success(f'Loaded {len(df):,} cleaned rows.')
    st.write('**Sample Rows**')
    st.dataframe(df.head())

    with st.spinner('Engineering RFM features...'):
        rfm = create_rfm(df)

    st.subheader('RFM Summary (first rows)')
    st.dataframe(rfm.head())

    with st.spinner('Clustering...'):
        rfm_labels, model, inertia, sil = fit_predict_kmeans(rfm, n_clusters=k)

    st.subheader('Cluster Metrics')
    c1, c2 = st.columns(2)
    with c1:
        st.metric('Inertia (lower is better)', f'{inertia:,.0f}')
    with c2:
        st.metric('Silhouette (−1 to 1, higher better)', f'{sil:.3f}')

    with st.spinner('Labelling segments...'):
        labeled = label_segments(rfm_labels)

    st.subheader('Segment Profiles')
    profile = labeled.groupby('SegmentLabel').agg({
        'Recency':'mean','Frequency':'mean','Monetary':['mean','count']
    }).round(2)
    st.dataframe(profile)

    st.subheader('Recommendations by Segment')
    st.dataframe(segment_recommendations())

    st.subheader('Customer → Cluster Mapping')
    st.dataframe(labeled[['CustomerID','Cluster','SegmentLabel']].head(20))

    # Download mapping CSV
    csv_bytes = labeled[['CustomerID','Cluster','SegmentLabel']].to_csv(index=False).encode('utf-8')
    st.download_button('Download Segment Mapping CSV', data=csv_bytes, file_name='customer_segments.csv', mime='text/csv')
else:
    st.info('Upload the dataset to begin.')
