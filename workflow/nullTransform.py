from logger import Logger

def nullTransform(df):
    Logger.loginfo("Checking nulls")

    df1 = df.dropna(thresh=df.shape[1] - 3)
    dropped_rows = df.index.difference(df1.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por tener más de 3 valores nulos:", dropped_rows)
    
    essential_columns = ["start_date", "end_date", "latitud", "longitud", "place_l2", "property_surface_total", "property_price", "property_currency"]

    df2 = df1[df1[essential_columns].notnull().all(axis=1)]
    dropped_rows = df1.index.difference(df2.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por tener valor nulo en una columna esencial:", dropped_rows)

    df3 = df2.dropna(subset=['property_rooms', 'property_bedrooms'], how='all')
    dropped_rows = df2.index.difference(df3.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por tener valor nulo en property_rooms Y property_bedrooms:", dropped_rows)

    # Imputación
    changed_rows = df3[df3["created_on"].isnull()].index.tolist()
    df3.loc[df3["created_on"].isnull(), "created_on"] = df3["start_date"]
    if not len(changed_rows) == 0:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en created_on:", changed_rows)

    changed_rows = df3[df3["operation"].isnull()].index.tolist()
    df3.loc[df3["operation"].isnull(), "operation"] = "Venta"
    if not len(changed_rows) == 0:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en operation:", changed_rows)

    rows_with_na_rooms = df3['property_rooms'].isna()
    changed_rows = rows_with_na_rooms.index.tolist()
    df3.loc[rows_with_na_rooms, 'property_rooms'] = df3.loc[rows_with_na_rooms, 'property_bedrooms']
    if not rows_with_na_rooms.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en property_rooms:", changed_rows)

    rows_with_na_bedrooms = df3['property_bedrooms'].isna()
    changed_rows = rows_with_na_rooms.index.tolist()
    df3.loc[rows_with_na_bedrooms, 'property_bedrooms'] = df3.loc[rows_with_na_bedrooms, 'property_rooms']
    if not rows_with_na_bedrooms.empty:
        Logger.logWarning("Las siguientes filas fueron imputadas con un nuevo valor en property_bedrooms:", changed_rows)

    return df3