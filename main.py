import pandas as pd

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
    df = consistencyTransform(df)
    df = outlierTransform(df)
    df = duplicateTransform(df)

    return df

def main():
    print("Starting..")

    df = extract()
    df = transform(df)
    print("Final shape: ", df.shape)

if __name__ == "__main__":
    main()
