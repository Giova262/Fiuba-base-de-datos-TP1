from logger import Logger
import pandas as pd

def consistencyTransform(df):
    #Change number in "property_rooms, bedrooms, surface_total and covered" to int
    df_transformed = df.copy()
    #col_to_convert = ["property_rooms", "property_bedrooms", "property_surface_total", "property_surface_covered"]
    #for column in col_to_convert:
        #df_transformed[column] = pd.to_numeric(df_transformed[column], errors='coerce')
        # Convert NaN values back to null
        #df_transformed[column] = df_transformed[column].astype('Int64')  # Use 'Int64' to preserve nulls
    #Change latitud, longitud and price to float
    col_to_convert = ["latitud", "longitud", "property_price"]
    for column in col_to_convert:
        df_transformed[column] = df_transformed[column].astype(float)

    #Change values to pandas date format, YYYY-MM-DD
    df_transformed['start_date'] = pd.to_datetime(df_transformed['start_date'])
    df_transformed['end_date'] = pd.to_datetime(df_transformed['end_date'])
    df_transformed['created_on'] = pd.to_datetime(df_transformed['created_on'])

    return df_transformed