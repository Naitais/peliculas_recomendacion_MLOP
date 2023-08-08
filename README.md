# peliculas_recomendacion_MLOP

En primera instancia, trabajé con dos datasets crudos sobre películas. Estos datos fueron procesados utilizando las librerias Numpy y Pandas. Seguido, con datasets ya limpios y separados, cree ciertas funciones para consultar datos con Fast API para a continuacion hacer el correspondiente deploy en Render. Finalmente, aplique un modelo de machine learning de clasificacion de arbol para crear un sistema de recomendacion de películas.

Explicar instrucciones de como se usa la api

Accediendo al siguiente link: https://sistema-de-recomendacion-de-peliculas-st65.onrender.com/docs#/

Cada función toma como input una entrada del usuario como por ejemplo el nombre de una película, el de un director o incluso un idioma y la función devuelve información sobre las películas.

Funciones:

1 peliculas_idioma --> devuelve cantidad de peliculas producidas en un idioma especifico
2 peliculas_duracion --> devuelve una pelicula con su duracion en minutos
3 franquicia --> devuelve cantidad de peliculas realizadas por la franquicia, ganancia total y ganancia promedio
4 pais --> devuelve cantidad de peliculas producidas en un pais 
5 productora --> devuelve cantidad de peliculas de productora y la ganancia total de la misma
6 info director --> devuelve grado de exito segun promedio de ganancias (si es mayor a 1 es exitoso) de un director en  especifico y listado de peliculas producidas por el mismo
7 modelo de recomendacion --> devuelve 5 peliculas similares a la que se introdujo como input

links de documentacion, herramientas utilizadas, librerias etc

informacion de contacto?

link de video explicativo de la api (subido a drive)