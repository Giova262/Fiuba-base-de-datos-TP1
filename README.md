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

## Workflow

El workflow se divide en distintas funciones que se encargan de mejorar cada fila de forma atómica. Cada función devuelve la fila (modificada si es el caso) y un booleano indicando si se debe descartar o no.

### 1. CheckNull
Descarta la fila si tiene más de dos campos en nulo, o no tiene valor en las columnas start_date, end_date, latitud, longitud, property_surface_total, property_price, o property_currency. En caso contrario, imputa los valores dependiendo de la columna.

Imputaciones:

 - created_on: se imputa con el valor que posea start_date ya que en la gran mayoría de las filas estos valores coinciden.
 - place_l2: se imputa utilizando una API de geolocalización y aportando la latitud y longitud.
 - place_l3: se imputa de la misma forma que __place_l2__.
 - operation: se interpreta que es una venta.
 - property_rooms: se interpreta que tiene una habitación, o se copia el valor de property_bedrooms si está disponible.
 - property_bedrooms: se imputa con el valor de property_rooms.

### 2. CheckType
Chequea que los datos de cada columna dentro de la fila sean consistentes con los definidos en la base de datos.
TODO resto de la documentación de esta función.

### 3. CheckConsistency
Chequea que los datos sean consistentes y tengan un valor lógico.
TODO resto de la documentación de esta función.

### 4. CheckOutliers
Chequea si hay valores fuera del rango establecido.
TODO resto de la documentación de esta función.

### 5. CheckDuplicated
Chequea si hay valores duplicados en las columnas establecidas (par longitud-latitud).
TODO resto de la documentación de esta función.