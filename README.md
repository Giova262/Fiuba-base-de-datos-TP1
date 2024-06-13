# TP ETL Base de Datos - FIUBA

Trabajo práctico para la materia Base de Datos (cátedra Merlino). [Enunciado](Enunciado.pdf)

## Alumnos

| Apellido | Nombre | Padrón |
| -------- | ------- | ------- |
| Velazquez | Joaquín Matías | 105980 |

# Tecnologías

Para este trabajo práctico se utilizará **pandas** para el manejo y transformación de datos, y **SQLite** como base de datos a la cuál cargar los datos transformados.

# Dataset

Se utiliza un dataset de las publicaciones de venta de propiedades en 2021.

## Columnas del dataset

| Columna Dataset | Columna SQLite | Tipo | Nulleable |
| -------- | ------- | ------- | ------- |
| start_date | start_date | TEXT* | No |
| end_date | end_date | TEXT* | Si |
| created_on | created_on | TEXT* | No |
| latitud | lat | REAL | No |
| longitud | lng | REAL | No |
| place_l2 | province | VARCHAR[30] | No |
| place_l3 | city | VARCHAR[30] | Si |
| operation | operation | VARCHAR[10] | No |
| property_type | type | VARCHAR[12] | No |
| property_rooms | rooms | INTEGER | No |
| property_bedrooms | bedrooms | INTEGER | No |
| property_surface_total | surface_total | INTEGER | No |
| property_surface_covered | surface_covered | INTEGER | Si |
| property_price | price | REAL | No |
| property_currency | currency | VARCHAR[4] | No |
| property_title | title | VARCHAR[200] | Si |

*SQLite no tiene una clase DATE, pero cuenta con una función para transformar una fecha a TEXT y viceversa.

### Columnas descartadas

 - **id:** como es un campo alfanumérico, se decidió descartarlo y agregar a la base de datos un nuevo campo id numérico.
 - **place_l4, place_l5 y place_l6:** estas columnas son nulas en la mayoría de los datos (>75%)

# Workflow

El workflow se divide en distintas secciones de código que reciben un DataFrame de pandas y devuelven un DataFrame transformado. 

## 1. NullTransform

### Filtro
Descarta la fila si tiene más de dos campos en nulo, o no tiene valor en las columnas *start_date*, *end_date*, *latitud*, *longitud*, *place_l2*, *property_surface_total*, *property_price*, o *property_currency*.

Además, no se tienen en cuenta las filas con valor nulo en *property_rooms* y *property_bedrooms*.

### Imputaciones
 - **created_on:** se imputa con el valor que posea start_date ya que en la gran mayoría de las filas estos valores coinciden.
 - **operation:** se interpreta que es una venta.
 - **property_rooms:** se imputa con el valor de *property_bedrooms*.
 - **property_bedrooms:** se imputa con el valor de *property_rooms*.

## 2. TypeTransform
Chequea que los datos de cada columna dentro de la fila sean consistentes con los definidos en la base de datos.
*TODO resto de la documentación de esta función.*

## 3. ConsistencyTransform
Chequea que los datos sean consistentes y tengan un valor lógico.
*TODO resto de la documentación de esta función.*

## 4. OutliersTransform
Chequea si hay valores fuera del rango establecido.
*TODO resto de la documentación de esta función.*

## 5. CheckDuplicated
Se mantiene una ocurrencia de los registros duplicados. Se dice registro duplicado al tener todos los campos con los mismos valores.