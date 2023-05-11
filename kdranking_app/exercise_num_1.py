# Este ejercicio tiene como objetivo ser una primera toma de contacto
# con la aplicacion Kwranking. Esta aplicacion es una aplicacion de 
# consola, es decir, se ejecutara desde el terminal. No hay que implentar
# mentar una interfaz grafica.

'''

Requisitos
Implementar un menú de aplicación con las siguientes opciones:

    [1] – Importar palabras clave
    [2] – Mostrar palabras clave
    [0] – Salir
    

Implementar una función carga_keywords() que lea un fichero llamado keywords.txt:

    El fichero tendrá una(s) palabra(s) clave por línea.
    No hay que separar las palabras clave con ningún carácter, solo enter.
    El fichero se leerá línea a línea, guardando la palabra clave correspondiente como un nuevo elemento de una lista.
    La función devolverá una lista de palabras clave.

-Cuando se introduzca la opción de menú [1], se invocará a la función carga_keywords(). La lista resultante se asignará a una variable del programa llamada keywords.
-Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras clave de 20 en 20, es decir, una vez mostradas 20 palabras clave, 
    el usuario deberá pulsar la tecla enter para ver las siguientes.
-Cuando se introduzca la opción de menú [0], el programa finalizará.

'''

import os

keywords = list()

def carga_keywords(keywords_txt):

    file_txt = open(keywords_txt, "r+")

    return file_txt.readlines()

def limpiar_pantalla():

    enter = input("\nPresione enter para continuar...")

    while(enter != ""):

        enter = input("\nPresione enter para continuar...")

    os.system("clear")

def print_lista(keywords_lista):

    os.system("clear")

    counter = 1

    number_of_twenties = 1

    for keyword in keywords_lista:

        print(f"{counter}.- {keyword}")

        if(number_of_twenties == 20):

            limpiar_pantalla()

            number_of_twenties = 1
        
        else:

            number_of_twenties += 1

        counter += 1

option = 1

while(option == 1 or option == 2):


    print("\n\tPress 1 for importing keywords\
        \n\tPress 2 for showing keywords\
        \n\tPress 0 for finishing\n")

    option = int(input("Select an option: "))

    if(option == 0): break

    elif(option == 1):

        keywords = carga_keywords("./keywords.txt")

        print("\n\tSe cargaron las keywords correctamente.")

        limpiar_pantalla()
    
    elif(option == 2):

        print()
        
        print_lista(keywords)

        limpiar_pantalla()

    else:

        print("\n\tSelect a valid option...")

        limpiar_pantalla()
          
        option = 1

os.system("clear")
        
print("Bye")