import pandas as pd

def label_segments(rfm_with_clusters: pd.DataFrame, cluster_col: str = 'Cluster') -> pd.DataFrame:
    """Assign human-readable labels to clusters based on Monetary and Recency heuristics."""
    prof = rfm_with_clusters.groupby(cluster_col).agg({'Recency':'mean','Frequency':'mean','Monetary':'mean'})
    prof = prof.rank(pct=True)  # percentile ranks
    labels = {}
    for c in prof.index:
        r, f, m = prof.loc[c, ['Recency','Frequency','Monetary']]
        if m > 0.75 and f > 0.75 and r < 0.3:
            labels[c] = 'Champions'
        elif m > 0.6 and r < 0.5:
            labels[c] = 'Loyal'
        elif r > 0.8:
            labels[c] = 'At Risk'
        elif m < 0.3 and f < 0.3:
            labels[c] = 'Low Value'
        else:
            labels[c] = 'Regulars'
    df = rfm_with_clusters.copy()
    df['SegmentLabel'] = df[cluster_col].map(labels)
    return df

def segment_recommendations() -> pd.DataFrame:
    data = [
        ('Champions','Upsell premium, early access, VIP perks'),
        ('Loyal','Loyalty rewards, cross-sell complementary items'),
        ('At Risk','Win-back discounts, personalized outreach'),
        ('Low Value','Awareness campaigns, bundles'),
        ('Regulars','Personalized recommendations, nudges to subscribe')
    ]
    return pd.DataFrame(data, columns=['Segment','RecommendedActions'])

def export_insights(summary_df: pd.DataFrame, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('# Segment Summary\n\n')
        f.write(summary_df.to_markdown())
        f.write('\n')
