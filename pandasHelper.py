from colorama import Fore, Style, init
import pandas as pd
import re

# Initialize colorama
init()


def is_number(value):
    if isinstance(value, (int, float, complex)):
        return True
    if isinstance(value, str):
        pattern = re.compile(r"^-?\d+(\.\d+)?$")
        return bool(pattern.match(value))
    return False


def is_null_but_not_zero(data):
    if data is None:  # Check if data is None (null)
        return True
    elif data == 0:  # Check if data is 0 (which is not considered null)
        return False
    else:  # For any other non-null value
        return False


def checkData():
    # Create a DataFrame
    df = pd.read_csv("dataset.csv")
    df = df.head()

    # Initialize an empty list to store transformed rows
    transformed_rows = []
    for index, row in df.iterrows():

        print(
            Fore.LIGHTBLUE_EX
            + "Row:"
            + str(index)
            + " processing data "
            + Style.RESET_ALL
        )
        for key in row.index:
            print(key + " " + str(row[key]))

            if is_null_but_not_zero(row[key]):
                print(
                    Fore.RED
                    + "Error: Row:"
                    + str(index)
                    + " , Column:"
                    + str(key)
                    + " Is empty"
                    + Style.RESET_ALL
                )
                return

            if key not in ["Date", "Symbol"] and not is_number(row[key]):
                print(
                    Fore.RED
                    + "Error: Row:"
                    + str(index)
                    + " , Column:"
                    + str(key)
                    + " It is not numerical"
                    + Style.RESET_ALL
                )
                return

        transformed_rows.append(
            {
                "id": row["id"],
                "Date": row["Date"],
                "Open": row["Open"],
                "High": row["High"],
                "Low": row["Low"],
                "Close": row["Close"],
                "Adj Close": row["Adj Close"],
                "Volume": row["Volume"],
                "Symbol": row["Symbol"],
            }
        )

        # print("#" + str(index) + " Fila correctamente validada data")
        print(
            Fore.GREEN + "Row:" + str(index) + " validated correctly" + Style.RESET_ALL
        )

    # Create a new DataFrame from the transformed rows
    df_transformed = pd.DataFrame(transformed_rows)
    print(df_transformed)
