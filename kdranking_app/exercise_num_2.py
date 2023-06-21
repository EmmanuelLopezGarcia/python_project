'''
Ejercicio #2: Comprobar la posición de una palabra clave en Google para un dominio en concreto
Categoría: Ejercicios
El objetivo de este ejercicio es determinar en qué posición rankea una palabra clave en Google para un dominio determinado.

Cuando realizas una búsqueda en Google para una serie de palabras clave, Google te muestra un listado de sitios web para los que esas palabras clave son relevantes.

Por ejemplo, la palabra Python para el dominio python.org rankea en la primera posición.

Por tanto, este ejercicio consiste en automatizar el proceso de encontrar la posición en que rankea una palabra clave en Google.

A continuación, te detallo en los requisitos cómo puedes implementar el ejercicio paso a paso.

---------------------------------------

Requisitos:

-Implementar una función comprueba_keywords(kw, dominio).

*Esta función define dos parámetros: kw es un string con la keyword o 
    keywords a buscar; dominio es el dominio para el que se quiere comprobar la posición 
    en que rankea la palabra clave kw.

*La función debe devolver la posición para la que rankean las palabras clave
    kw para el dominio dominio.

*Si no se ha encontrado en las primeras 100 posiciones, la función devolverá por 
    defecto el valor 100.

*Añadir una variable al programa con el dominio a tener en cuenta (puedes elegir 
    el dominio que prefieras para trabajar).

*Añadir una nueva opción de menú al programa: [3] - Comprobar palabras clave.

*Cuando el usuario seleccione en el menú la opción 3, el programa solicitará al 
    usuario qué palabras clave quiere comprobar y seguidamente invocará a la 
    función comprueba_keywords().

*Además, se mostrará en qué posición rankean las palabras clave o si no rankean 
    (la función devuelve el valor 100).

'''

import requests

resp = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

print(resp.json())
