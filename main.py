from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

if __name__ == "__main__":
    df = extract_data('data/raw/orders.csv')
    cleaned_df = transform_data(df)
    cleaned_df.to_csv('data/processed/cleaned_orders.csv', index=False)
    load_data(cleaned_df, 'database/orders.db')
    print("ETL process completed successfully.")
