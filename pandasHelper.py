import pandas as pd


def pandasVerifyInstallation():
    # Create a DataFrame
    df = pd.read_csv("1000_cryptos.csv")
    
    for index, row in df.iterrows():
        print(f"Index: {index}")
        print(f"Row: {row}")
