import pandas as pd

def transform_data(df):
    df = df.dropna()
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df = df.dropna(subset=['order_date'])
    return df
