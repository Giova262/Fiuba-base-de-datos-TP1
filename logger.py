from colorama import Fore, Style, init
import logging

# Basic configuration for the logger
logging.basicConfig(
    level=logging.DEBUG,  # Set the log level to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler(),  # Also log to console
    ],
)

logger = logging.getLogger(__name__)

class Logger:

    def logWarning(message, indexList):
        logger.critical(message + '\n' + str(indexList))
        # print(Fore.LIGHTBLUE_EX + "Row:" + str(index) + message + Style.RESET_ALL)

    def logError(message, indexList):
        logger.error(message + '\n' + str(indexList))
        # print(Fore.RED + "Row:" + str(index) + message + Style.RESET_ALL)

    def logSuccess(message, indexList):
        logger.info(message + '\n' + str(indexList))
        # print(Fore.GREEN + "Row:" + str(index) + message + Style.RESET_ALL)
    
    def loginfo(message):
        logger.info(message + '\n')
        # print(Fore.GREEN + "Row:" + str(index) + message + Style.RESET_ALL)