import pandas as pd

def clean_sales_data(filepath):
    df = pd.read_csv(filepath)
    # Example cleaning: drop missing values and remove duplicates
    df = df.dropna()
    df = df.drop_duplicates()
    df.to_csv(filepath, index=False)
    print("Data cleaned and saved:", filepath)

if __name__ == "__main__":
    clean_sales_data("../data/sales.csv")