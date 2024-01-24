from pyspark.sql import SparkSession
from messages import show_welcome, show_menu,show_exit, show_reading_sucess
from utilities import printsep
from constants import OptionsList, Numbers
import logging
import getpass

logging.getLogger("py4j").setLevel(logging.ERROR)
logging.getLogger("pyspark").setLevel(logging.ERROR)
spark = SparkSession.builder.appName("Fido").getOrCreate()
from sparkfunctions import readInput
if __name__ == "__main__":
    show_welcome()
    while True:
        printsep()
        show_menu()
        try:
            inputOption = getpass.getpass("")
        except KeyboardInterrupt:
            show_exit()
            break
        if inputOption == Numbers.Three:
            show_exit()
            break
        elif inputOption in OptionsList:
            evalDataFrame = readInput(spark= spark, option= inputOption)
            show_reading_sucess()
            break
        else:
            print("Opción no válida.")
