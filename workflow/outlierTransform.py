from logger import Logger

def outlierTransform(df):
    # Elimina las filas que tengan una fecha de fin posterior a la fecha de inicio
    df_transformed = df.copy()
    df_transformed = df_transformed[df_transformed['end_date'].isnull() | (df_transformed['end_date'] <= df_transformed['start_date'])]
    
    # Elimina los valores de latitud y longitud ilógicos
    df_transformed = df_transformed[(df_transformed['latitud'] < 90) & (df_transformed['latitud'] > -90) ]
    df_transformed = df_transformed[(df_transformed['longitud'] < 180) & (df_transformed['longitud'] > -180) ]

    # Elimina filas de propiedades que no tengan un tipo correcto
    df_transformed = df_transformed[df_transformed['property_type'].isin(['PH', 'Casa', 'Departamento'])]

    return df