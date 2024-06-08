from logger import Logger

def nullTransform(df):
    df1 = df.dropna(thresh=df.shape[1] - 3)
    dropped_rows = df.loc[df.index.difference(df1.index)]
    if not dropped_rows.empty:
        Logger.logError("Las siguientes filas fueron eliminadas por tener más de 3 valores nulos:", dropped_rows)
    
    essential_columns = ["start_date", "end_date", "latitud", "longitud", "place_l2", "property_surface_total", "property_price", "property_currency"]

    df2 = df1[df1[essential_columns].notnull().all(axis=1)]
    dropped_rows = df1.loc[df1.index.difference(df2.index)]
    if not dropped_rows.empty:
        Logger.logError("Las siguientes filas fueron eliminadas por tener valor nulo en una columna esencial:", dropped_rows[essential_columns])

    df3 = df2.dropna(subset=['property_rooms', 'property_bedrooms'], how='all')
    dropped_rows = df2.loc[df2.index.difference(df3.index)]
    if not dropped_rows.empty:
        Logger.logError("Las siguientes filas fueron eliminadas por tener valor nulo en property_rooms Y property_bedrooms:", dropped_rows[["property_rooms", "property_bedrooms"]])

    # Imputación
    changed_rows = df3[df3["created_on"].isnull()].copy()
    df3.loc[df3["created_on"].isnull(), "created_on"] = df3["start_date"]
    if not changed_rows.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en created_on:", changed_rows["created_on"])

    changed_rows = df3[df3["operation"].isnull()].copy()
    df3.loc[df3["operation"].isnull(), "operation"] = "Venta"
    if not changed_rows.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en operation:", changed_rows["operation"])

    rows_with_na_rooms = df3['property_rooms'].isna()
    df3.loc[rows_with_na_rooms, 'property_rooms'] = df3.loc[rows_with_na_rooms, 'property_bedrooms']
    if not rows_with_na_rooms.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en property_rooms:", df3.loc[rows_with_na_rooms, 'property_rooms'])

    rows_with_na_bedrooms = df3['property_bedrooms'].isna()
    df3.loc[rows_with_na_bedrooms, 'property_bedrooms'] = df3.loc[rows_with_na_bedrooms, 'property_rooms']
    if not rows_with_na_bedrooms.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en property_bedrooms:", df3.loc[rows_with_na_bedrooms, 'property_bedrooms'])

    return df3