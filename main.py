from db.databaseHelper import (
    create_connection,
    create_table,
    insert_user,
    select_all_users,
)
from pandasHelper import checkData
import pandas as pd

from workflow.nullTransform import NullTransform
from workflow.typeTransform import TypeTransform
from workflow.consistencyTransform import ConsistencyTransform
from workflow.outlierTransform import OutlierTransform
from workflow.duplicateTransform import DuplicatedTransform

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
    nullTransform = NullTransform()
    typeTransform = TypeTransform()
    consistencyTransform = ConsistencyTransform()
    outlierTransform = OutlierTransform()
    duplicatedTransform = DuplicatedTransform()

    df = df.apply(nullTransform.transform)
    df = df.apply(typeTransform.transform)
    df = df.apply(consistencyTransform.transform)
    df = df.apply(outlierTransform.transform)
    df = df.apply(duplicatedTransform.transform)

    return df

def main():
    print("Starting..")

    df = extract()
    df = transform(df)

if __name__ == "__main__":
    main()
