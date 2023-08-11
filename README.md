# peliculas_recomendacion_MLOP

En primera instancia, trabajé con dos datasets crudos sobre películas. Estos datos fueron procesados utilizando las librerias Numpy, Pandas, sklearn, csv y FastAPI. Seguido, con datasets ya limpios y separados, cree ciertas funciones para consultar datos con Fast API para a continuacion hacer el correspondiente deploy en Render. Finalmente, aplique un modelo de machine learning de clasificacion de arbol para crear un sistema de recomendacion de películas.

*ETL*

Al trabajar con los datos habian muchas columnas anidadas dentro de diccionarios que a su vez tenían más columnas dentro por lo que cree algunas funciones a parte para poder procesar los datos que contenían. Al terminar de limpiar los datos arme distintos datasets para cada función de mi API.

*EDA*

Mi EDA fue bastante superficial ya que solo revise cosas básicas como la cantidad de nulos, la calidad de datos de ciertas columnas con respecto a mi objetivo, la variabilidad de las columnas, ciertos valores extraños o erroneos en algunos campos, las palabras más repetidas en la columna movie_title y overview, entre otras características de los datasets que manipule.

*FastAPI y Render*

Deployee mi API en Render y las funciones fueron creadas utilizando FastAPI. Cada función toma como input una entrada del usuario como por ejemplo el nombre de una película, el de un director o incluso un idioma y la función devuelve información sobre las películas. 

API deployada en el siguiente link: https://sistema-de-recomendacion-de-peliculas-st65.onrender.com/docs#/ 

_Breve descripcion de las funciones:_

- Peliculas_idioma --> devuelve cantidad de peliculas producidas en un idioma especifico

- Peliculas_duracion --> devuelve una pelicula con su duracion en minutos

- Franquicia --> devuelve cantidad de peliculas realizadas por la franquicia, ganancia total y ganancia promedio

- Pais --> devuelve cantidad de peliculas producidas en un pais 

- Productora --> devuelve cantidad de peliculas de productora y la ganancia total de la misma

- Info director --> devuelve grado de exito segun promedio de ganancias (si es mayor a 1 es exitoso) de un director en  especifico y listado de peliculas producidas por el mismo

- Modelo de recomendacion --> devuelve 5 peliculas similares a la que se introdujo como input


_link de video explicativo de la api (subido a drive)_