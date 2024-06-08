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

def main():
    print("Starting..")

    df = extract()
    print(df.head())

def extract():
    return pd.read_csv("dataset.csv", usecols = ["id"])

def transform(df):
    nullCheck = NullCheck()
    typeCheck = TypeCheck()
    consistencyCheck = ConsistencyCheck()
    outlierCheck = OutlierCheck()
    duplicatedCheck = DuplicatedCheck()

    new_df = pd.DataFrame()
    for index, row in df.iterrows():
        (nullResult, keep) = NullCheck.check(row)
        if not keep:
            continue
        (typeResult, keep) = TypeCheck.check(nullResult)
        if not keep:
            continue
        (consistencyResult, keep) = ConsistencyCheck.check(typeResult)
        if not keep:
            continue
        (outlierResult, keep) = OutlierCheck.check(consistencyResult)
        if not keep:
            continue
        (duplicatedResult, keep) = DuplicatedCheck.check(outlierResult)
        if not keep:
            continue
        new_df.append(duplicatedResult)
    return new_df

if __name__ == "__main__":
    main()
