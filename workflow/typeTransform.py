from logger import Logger
import pandas as pd
import re

def is_number(value):
        if isinstance(value, (int, float, complex)):
            return True
        if isinstance(value, str):
            pattern = re.compile(r"^-?\d+(\.\d+)?$")
            return bool(pattern.match(value))
        return False
    
def is_text(data):
    return isinstance(data, str)

def typeTransform(df):
    Logger.loginfo("Checking types")

    df1 = df[df['latitud'].apply(lambda x: is_number(x))]
    dropped_rows = df.index.difference(df1.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en latitud:", dropped_rows)

    df2 = df1[df1['longitud'].apply(lambda x: is_number(x))]
    dropped_rows = df1.index.difference(df2.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en longitud:", dropped_rows)

    df3 = df2[df2['place_l2'].apply(lambda x: is_text(x))]
    dropped_rows = df2.index.difference(df3.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en place_l2:", dropped_rows)

    df4 = df3[df3['place_l3'].apply(lambda x: is_text(x))]
    dropped_rows = df3.index.difference(df4.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en place_l2:", dropped_rows)

    df5 = df4[df4['operation'].apply(lambda x: is_text(x))]
    dropped_rows = df4.index.difference(df5.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en operation:", dropped_rows)

    df6 = df5[df5['operation'].apply(lambda x: is_text(x))]
    dropped_rows = df5.index.difference(df6.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en operation:", dropped_rows)

    df7 = df6[df6['property_rooms'].apply(lambda x: is_number(x))]
    dropped_rows = df6.index.difference(df7.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_rooms:", dropped_rows)
    
    df8 = df7[df7['property_bedrooms'].apply(lambda x: is_number(x))]
    dropped_rows = df7.index.difference(df8.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_bedrooms:", dropped_rows)

    df9 = df8[df8['property_surface_total'].apply(lambda x: is_number(x))]
    dropped_rows = df8.index.difference(df9.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_surface_total:", dropped_rows)

    df10 = df9[df9['property_surface_covered'].apply(lambda x: is_number(x))]
    dropped_rows = df9.index.difference(df10.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_surface_covered:", dropped_rows)

    df11 = df10[df10['property_price'].apply(lambda x: is_number(x))]
    dropped_rows = df10.index.difference(df11.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_price:", dropped_rows)

    df12 = df11[df11['property_currency'].apply(lambda x: is_text(x))]
    dropped_rows = df11.index.difference(df12.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_currency:", dropped_rows)

    df13 = df12[df12['property_title'].apply(lambda x: is_text(x))]
    dropped_rows = df12.index.difference(df13.index).tolist()
    if not len(dropped_rows) == 0:
        Logger.logError("Las siguientes filas fueron eliminadas por no tener valor de texto en property_title:", dropped_rows)

    return df