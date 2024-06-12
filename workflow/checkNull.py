from logger import Logger

class NullCheck:
    
    def is_null_but_not_zero(self, data):
        if data is None:  # Check if data is None (null)
            return True
        elif data == 0:  # Check if data is 0 (which is not considered null)
            return False
        else:  # For any other non-null value
            return False
        
    def check(self, index, row):
        print('chequeando Nulls..')
        for key in row.index:
            if self.is_null_but_not_zero(row[key]):
                Logger.logError(index, " " + str(key) + " is empty")
                return (row, False)

        Logger.logSuccess(index, " Nulls are OK")
        return (row, True)