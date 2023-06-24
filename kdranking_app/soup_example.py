from bs4 import BeautifulSoup

contenido = """ 

    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Página de prueba</title>
    </head>
    <body>
    <div id="main" class="full-width">
        <h1>El título de la página</h1>
        <p>Este es el primer párrafo</p>
        <p>Este es el segundo párrafo</p>
        <div id="innerDiv">
            <div class="links">
                <a href="https://pagina1.xyz/">Enlace 1</a>
                <a href="https://pagina2.xyz/">Enlace 2</a>
            </div>
            <div class="right">
                <div class="links">
                    <a href="https://pagina3.xyz/">Enlace 3</a>
                    <a href="https://pagina4.xyz/">Enlace 4</a>
                </div>
            </div>
        </div>
        <div id="footer">
            <!-- El footer -->
            <p>Este párrafo está en el footer</p>
            <div class="links footer-links">
                <a href="https://pagina5.xyz/">Enlace 5</a>
            </div>
        </div>
    </div>
    </body>
    </html>

"""

# Creando el objeto "soup" con BeautifulSoup
# El parser es lxml

soup = BeautifulSoup(contenido, 'lxml')

#print(soup.title)

"""
Accediendo a los atributos div por medio de la propiedad "div"

div_main = soup.div

print(div_main.attrs)

print(div_main['class'])

"""

"""

Accediendo a los atributos p por medio de pa propiedad "string"

primer_parrafo = soup.p

texto = primer_parrafo.string

print(texto)

"""

"""

# Accediendo a los hijos con los objetos "contents" "children" y "descendants"

# El atributo "contents: Devuelve una lista con todos los hijos de primer nivel de un objeto"

# El generador "children: Devuelve un iterador para recorrer los hijos del primer nivel de un objeto"

# El generador descendants: Este atributo devuelve un irerador que permite recorrer todos los
# hijos de un objeto. No importa el nivel de anidamiento.

# Vamos a acceder a todos los hijos del bloque div con id='innerDiv'

inner_div = soup.div.div

# "contents"

hijos = inner_div.contents

for child in hijos:

    if child.name:

        print(f'{child.name}')

# "children"

hijos_iterables = inner_div.children

for child in hijos_iterables:

    if child.name:
        
        print(f'{child.name}')

# "descendants"

todos_los_hijos_iterables = inner_div.descendants

for child in todos_los_hijos_iterables:

    if child.name:

        print(f"{child.name}")
        
"""

