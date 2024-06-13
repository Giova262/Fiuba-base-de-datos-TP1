from logger import Logger

def duplicateTransform(df):
    #Remove exact duplicates, keep the first occurrence
    duplicated_rows = df[df.duplicated(keep='first')].to_dict(orient='records')
    df_without_diuplicated = df.drop_duplicates(keep='first')
    if len(duplicated_rows):
        Logger.logWarning("Las siguientes filas fueron eliminadas al ser duplicados exactos:", duplicated_rows)

    return df_without_diuplicated