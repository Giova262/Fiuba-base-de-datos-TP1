import pandas as pd
from logger import Logger
from db.databaseHelper import setDB, create_table, insert_property_post, get_count

from workflow.nullTransform import nullTransform
from workflow.typeTransform import typeTransform
from workflow.consistencyTransform import consistencyTransform
from workflow.outlierTransform import outlierTransform
from workflow.duplicateTransform import duplicateTransform

def extract():
    cols_to_keep = ["start_date",
                    "end_date",
                    "created_on",
                    "latitud",
                    "longitud",
                    "place_l2",
                    "place_l3",
                    "operation",
                    "property_type",
                    "property_rooms",
                    "property_bedrooms",
                    "property_surface_total",
                    "property_surface_covered",
                    "property_price",
                    "property_currency",
                    "property_title"]
    
    return pd.read_csv("dataset.csv", usecols=cols_to_keep)

def transform(df):
    df = nullTransform(df)
    df = typeTransform(df)
    # df = consistencyTransform(df)
    df = outlierTransform(df)
    df = duplicateTransform(df)

    Logger.loginfo(f"Final shape: {df.shape}")

    return df

def load(df):
    conn = setDB()
    create_table(conn)
    for index, row in df.iterrows():
        property_post = tuple(row)
        last_row_id = insert_property_post(conn, property_post)
        if last_row_id is not None:
            Logger.loginfo(f"Se cargó la fila {last_row_id}")
        else:
            Logger.logError("No se pudo cargar la fila:", index)
    print(get_count(conn))

def main():
    print("Starting..")

    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
