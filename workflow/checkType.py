from logger import Logger
import re


# | start_date | start_date | TEXT* | No |
# | end_date | end_date | TEXT* | Si |
# | created_on | created_on | TEXT* | No |
# | latitud | lat | REAL | No |
# | longitud | lng | REAL | No |
# | place_l2 | province | VARCHAR[30] | No |
# | place_l3 | city | VARCHAR[30] | Si |
# | operation | operation | VARCHAR[10] | No |
# | property_type | type | VARCHAR[12] | No |
# | property_rooms | rooms | INTEGER | No |
# | property_bedrooms | bedrooms | INTEGER | No |
# | property_surface_total | surface_total | INTEGER | No |
# | property_surface_covered | surface_covered | INTEGER | Si |
# | property_price | price | REAL | No |
# | property_currency | currency | VARCHAR[4] | No |
# | property_title | title | VARCHAR[200] | Si |


class TypeCheck:

    def is_number(self, value):
        if isinstance(value, (int, float, complex)):
            return True
        if isinstance(value, str):
            pattern = re.compile(r"^-?\d+(\.\d+)?$")
            return bool(pattern.match(value))
        return False
    
    def is_text(self, data):
        return isinstance(data, str)

    def check(self, index, row):
        Logger.loginfo("Row:" + str(index) + " Checking Types")
        for key in row.index:
            if key == "start_date":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "end_date":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "created_on":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "latitud":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "longitud":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "place_l2":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "place_l3":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "operation":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_type":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_rooms":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_bedrooms":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_surface_total":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_surface_covered":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_price":
                if not self.is_number(row[key]):
                    Logger.logError(index, " " + str(key) + " is not NUMBER - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_currency":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)
            elif key == "property_title":
                if not self.is_text(row[key]):
                    Logger.logError(index, " " + str(key) + " is not TEXT - Value: " + str(row[key]))
                    return (row, False)

        Logger.logSuccess(index, " Types are OK")
        return (row, True)
