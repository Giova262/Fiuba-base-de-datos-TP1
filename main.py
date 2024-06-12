from db.databaseHelper import (
    create_connection,
    create_table,
    insert_user,
    select_all_users,
)
from pandasHelper import checkData
import pandas as pd

from workflow.checkNull import NullCheck
from workflow.checkType import TypeCheck
from workflow.checkConsistency import ConsistencyCheck
from workflow.checkOutlier import OutlierCheck
from workflow.checkDuplicated import DuplicatedCheck


def extract():
    print("Extracting...")
    return pd.read_csv(
        "dataset.csv",
        usecols=[
            "start_date",
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
            "property_title",
        ],
    )


def transform(df):

    print("Transforming...")
    nullCheck = NullCheck()
    typeCheck = TypeCheck()
    consistencyCheck = ConsistencyCheck()
    outlierCheck = OutlierCheck()
    duplicatedCheck = DuplicatedCheck()

    new_df = []
    for index, row in df.iterrows():

        (nullResult, keep) = nullCheck.check(index, row)
        if not keep:
            continue
        
        (typeResult, keep) = typeCheck.check(nullResult)
        if not keep:
            continue

        (consistencyResult, keep) = consistencyCheck.check(typeResult)
        if not keep:
            continue

        (outlierResult, keep) = outlierCheck.check(consistencyResult)
        if not keep:
            continue

        (duplicatedResult, keep) = duplicatedCheck.check(outlierResult)
        if not keep:
            continue

        new_df.append(duplicatedResult)

    return new_df


def main():
    df = extract()
    df = df.head()
    transform(df)
    # print(df.head())

if __name__ == "__main__":
    main()
