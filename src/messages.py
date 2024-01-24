from constants import *
from utilities import printnl

def show_welcome():
    print(welcomeMsg)

def show_menu():
    printnl()
    print("1. CSV")
    print("2. Parquet")
    print("3. Salir")

def show_reading_failure():
    print("Error en la lectura, revise los datos")

def show_exit():
    print("Saliendo del programa. ¡Hasta luego!")

def show_reading_sucess():
    print("La lectura fue correctamente realizada")