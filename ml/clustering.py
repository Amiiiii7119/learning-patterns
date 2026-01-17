from sklearn.cluster import KMeans
import pandas as pd

def cluster_students(df_original, df_scaled, k=4):
    model = KMeans(n_clusters=k, random_state=42)
    clusters = model.fit_predict(df_scaled)

    df_original["learning_cluster"] = clusters
    return df_original, model
