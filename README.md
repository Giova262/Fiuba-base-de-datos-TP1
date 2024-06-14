# TP ETL Base de Datos - FIUBA

Trabajo práctico para la materia Base de Datos (cátedra Merlino). [Enunciado](Enunciado.pdf)

## Alumnos

| Apellido | Nombre | Padrón |
| -------- | ------- | ------- |
| Velazquez | Joaquín Matías | 105980 |
| Giovanni Valdivia | Josué | 93075 |
| Ledesma | Dylan | 102876 |
| Rea | Matías | 99770 |

# Tecnologías

Para este trabajo práctico se utilizará **pandas** para el manejo y transformación de datos, y **SQLite** como base de datos a la cuál cargar los datos transformados.

## Requisitos
### pandas

```bash
pip install pandas
```
### colorama

```bash
pip install colorama
```

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
| place_l2 | province | VARCHAR[30] | Si |
| place_l3 | city | VARCHAR[30] | Si |
| operation | operation | VARCHAR[10] | No |
| property_type | type | VARCHAR[12] | No |
| property_rooms | rooms | INTEGER | No |
| property_bedrooms | bedrooms | INTEGER | No |
| property_surface_total | surface_total | INTEGER | No |
| property_surface_covered | surface_covered | INTEGER | Si |
| property_price | price | REAL | No |
| property_currency | currency | VARCHAR[4] | No |
| property_title | title | VARCHAR[200] | No |

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

## 3. OutliersTransform
Chequea si hay valores fuera del rango establecido.

### start_date y end_date
Elimina cualquier fila que tenga un start_date posterior al end_date.

### latitud y longitud
Se eliminan también las filas que tengan valores de latitud mayor a 90 o menores a -90, y lo mismo con longitud y 180/-180.

### property_type
Se eliminan las filas que tienen un tipo de propiedad incorrecto.

## 4. CheckDuplicated
Se mantiene una ocurrencia de los registros duplicados. Se dice registro duplicado al tener todos los campos con los mismos valores.
