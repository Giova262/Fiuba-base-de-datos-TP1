from workflow.checkNull import NullCheck
from workflow.checkType import TypeCheck
from workflow.checkConsistency import ConsistencyCheck
from workflow.checkOutlier import OutlierCheck
from workflow.checkDuplicated import DuplicatedCheck
from logger import Logger
import pandas as pd


def extract():
    Logger.loginfo(" Starting ETL")
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
    nullCheck = NullCheck()
    typeCheck = TypeCheck()
    outlierCheck = OutlierCheck()
    duplicatedCheck = DuplicatedCheck()
    consistencyCheck = ConsistencyCheck()

    new_df = []
    new_df_with_erros = []
    for index, row in df.iterrows():
        (rowTemp, keep) = nullCheck.check(index, row)
        if not keep:
            new_df_with_erros.append(rowTemp)
            continue

        (rowTemp, keep) = typeCheck.check(index, rowTemp)
        if not keep:
            new_df_with_erros.append(rowTemp)
            continue

        (rowTemp, keep) = consistencyCheck.check(index, rowTemp)
        if not keep:
            new_df_with_erros.append(rowTemp)
            continue

        (rowTemp, keep) = outlierCheck.check(index, rowTemp)
        if not keep:
            new_df_with_erros.append(rowTemp)
            continue

        (rowTemp, keep) = duplicatedCheck.check(index, rowTemp)
        if not keep:
            new_df_with_erros.append(rowTemp)
            continue

        new_df.append(rowTemp)

    return new_df


def main():
    df = extract()
    df = df.head()
    transform(df)


if __name__ == "__main__":
    main()
