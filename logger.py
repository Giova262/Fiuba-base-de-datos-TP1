
from colorama import Fore, Style, init

class Logger:
    
    def logWarning(index, message):
        print(
            Fore.LIGHTBLUE_EX
            + "Row:"
            + str(index)
            + message
            + Style.RESET_ALL
        )

    def logError(index, message):
        print(
            Fore.RED
            + "Row:"
            + str(index)
            + message
            + Style.RESET_ALL
        )

    def logSuccess(index, message):
        print(
            Fore.GREEN
            + "Row:"
            + str(index)
            + message
            + Style.RESET_ALL
        )