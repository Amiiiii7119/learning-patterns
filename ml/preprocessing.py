import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    # Drop target leakage (final grade not used for clustering)
    target_cols = ["G3"]
    df_features = df.drop(columns=target_cols)

    # Encode categorical columns
    cat_cols = df_features.select_dtypes(include=["object"]).columns
    encoder = LabelEncoder()
    for col in cat_cols:
        df_features[col] = encoder.fit_transform(df_features[col])

    # Scale numeric features
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_features)

    return df, df_scaled
