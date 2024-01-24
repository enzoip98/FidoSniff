from pyspark.sql import SparkSession
from messages import show_reading_failure
def readInput(spark:SparkSession,option:str):
    match option:
        case "1":
            while True:
                path = input("Escriba la ruta del archivo CSV: ")
                delimiter = input("Escriba el separador: ")
                try:
                    df = spark.read.option("header",True).option("delimiter",delimiter).csv(path)
                    break
                except:
                    show_reading_failure()
            return df
        case "2":
            while True:
                path = input("Escriba la ruta del archivo Parquet: ")
                try:
                    df =  spark.read.parquet(path)
                    break
                except:
                    show_reading_failure()
            return df