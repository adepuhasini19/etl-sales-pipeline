import pandas as pd 
def extract():
    print("Extracting data...")
    df =pd.read_csv("data/sales_data.csv")
    return df
def transform(df):
    print("Transforming data...")

    df = df.dropna()
    df['data'] = pd.to_datetime(df['date'])
    df['total_price'] = df['quantity'] * df['price']

    return df
def load(df):
    print("Loading data...")
    df.to_csv("data/cleaned_sales_data.csv", index=False)
    print("ETL Completed Successfully!")

def main():
    data = extract()
    transformed = transform(data)
    load(transformed)

if __name__ == "__main__":
    main()        