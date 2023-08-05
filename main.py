from fastapi import FastAPI
import csv , locale, pandas as pd

locale.setlocale(locale.LC_TIME, 'es_ES') #importo locale y seteo idioma para que los meses salgan en español

app = FastAPI()

#considerar aramr csvs especificos para cada funcion

@app.get("/")
def home():
    return {"HOME": "home"}

#cargo csv limpio en una lista con cada row como diccionario
#VOY A TENER QUE ELIMINAR ESTA FUNCION PORQUE SOLO TIENEN QUE HABER 6
def load_movies():
    movies = []
    with open(r"datasets\datasets_limpios\dfMovies.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append(row)
        movies=pd.DataFrame(movies)
        return movies

#def cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
#   Ejemplo de retorno: X cantidad de películas fueron estrenadas en el mes de X

@app.get("/movies/peliculas_mes/{Mes}") #decorator
def cantidad_filmaciones_mes(Mes):
    meses=["enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio","agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if Mes in meses:
        movies = load_movies()
        movies["release_date"] = pd.to_datetime(movies["release_date"], format="%Y-%m-%d")
        month = movies["release_date"].dt.strftime("%B")
        result = movies[month == Mes.lower()]
        result=result["release_date"].count().item() #uso la funcion .item() para convertir en int 
                                                    #nativo de python y no tener errores
                                                    #al pasar una variable de numpy
        return f"En el mes de {(Mes).lower()} se estrenaron {result} películas."
    else:
        return f"ERROR: '{(Mes).capitalize()}' no es un mes valido. Intente nuevamente."
    
#copio la misma estructura de la funcion de meses y la adapto para que tome dias de la semana
@app.get("/movies/peliculas_dias/{Dia}") #decorator
def cantidad_filmaciones_dia(Dia):
    dias=["lunes","martes","miercoles", "jueves", "viernes", "sabado", "domingo"]
    if Dia in dias:
        movies = load_movies()
        movies["release_date"] = pd.to_datetime(movies["release_date"], format="%Y-%m-%d")
        dia = movies["release_date"].dt.strftime("%A")
        result = movies[dia == Dia.lower()]
        result=result["release_date"].count().item() #uso la funcion .item() para convertir en int 
                                                    #nativo de python y no tener errores
                                                    #al pasar una variable de numpy
        return f"En los dias {(Dia).lower()} se estrenaron {result} películas."
    else:
        return f"ERROR: '{(Dia).capitalize()}' no es un día valido. Intente nuevamente."

#def score_titulo( titulo_de_la_filmación ): Se ingresa el título de una filmación esperando 
#como respuesta el título, el año de estreno y el score.
    #Ejemplo de retorno: La película X fue estrenada en el año X con un score/popularidad de X

@app.get("/movies/peliculas_score/{titulo_de_la_filmación}") #decorator
def score_titulo( titulo_de_la_filmación ):
    movies = load_movies()
    title=movies.loc[movies.movie_title == titulo_de_la_filmación, ["movie_title"]]
    year=movies.loc[movies.movie_title == titulo_de_la_filmación, ["release_year"]]
    popularity=movies.loc[movies.movie_title == titulo_de_la_filmación, ["popularity"]]
    return f"La película titulada {(title).capitalize} se estreno en el año {year} y tiene un puntaje de popularidad de {popularity}."

#TODAS LAS FUNCIONES QUE ESTAN ARRIBA LAS TENGO QUE ELIMINAR PORQUE ME EQUIVOQUE DE CONSIGNAS Y SON LAS DE
#LA COHORTE ANTERIOR XD


#-------------------------------------------------------------------------------------------------------#
######################################## PRIEMRA FUINCION ###############################################
#-------------------------------------------------------------------------------------------------------#



#Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). 
#Debe devolver la cantidad de películas producidas en ese idioma.
#   Ejemplo de retorno: X cantidad de películas fueron estrenadas en idioma

@app.get("/movies/peliculas_idioma/{Idioma}") #decorator
def peliculas_idioma( Idioma: str ):
    Idioma =Idioma.lower() #lo convierto a lower case para evitar errores en el input

    dfPeliculasIdiomas = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfPeliculasIdiomas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfPeliculasIdiomas.append(row)
    #transformo resultado en df
    dfPeliculasIdiomas=pd.DataFrame(dfPeliculasIdiomas)

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    idiomasCorto = set([i for i in dfPeliculasIdiomas.original_language]) 

    if Idioma in idiomasCorto: #utilizo los idiomas para tener algo de error handling cuando el input no esta en la lista de idiomas
        cantidadPels=dfPeliculasIdiomas.loc[dfPeliculasIdiomas.original_language == Idioma, ["original_language"]].count()
        cantidadPels= cantidadPels.iloc[0]
        return f"La cantidad de películas estrenadas en idioma '{Idioma}' es {cantidadPels}."
    else: 
        return f"ERROR: '{(Idioma).capitalize()}' no es un idioma valido. Ejemplo de idioma valido: en, es, fr, etc. Intente nuevamente."


#-------------------------------------------------------------------------------------------------------#
######################################## SEGUNDA FUINCION ###############################################
#-------------------------------------------------------------------------------------------------------#

#def peliculas_duracion( Pelicula: str ): Se ingresa una pelicula. Debe devolver la duracion y el año.
#Ejemplo de retorno: X . Duración: x. Año: xx

@app.get("/movies/peliculas_duracion/{Pelicula}") #decorator
def peliculas_duracion( Pelicula: str ):

    dfMoviesDuration = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfMoviesduration.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfMoviesDuration.append(row)
    #transformo resultado en df
    dfMoviesDuration=pd.DataFrame(dfMoviesDuration)

    #cambio a lowercase para que no hayan errores de capitalizacion en el input de mi funcion
    dfMoviesDuration["movie_title"] = dfMoviesDuration["movie_title"].str.lower()
    Pelicula = Pelicula.lower()

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    titulos = set([i for i in dfMoviesDuration.movie_title])

    #utilizo los idiomas para tener algo de error handling cuando el input no esta en la lista de idiomas
    if Pelicula in titulos: 
        #busco la duracion en minutos de la pelicula
        movieDuration=dfMoviesDuration.loc[dfMoviesDuration["movie_title"] == Pelicula, ["runtime"]]
        movieDuration=movieDuration.iloc[0, 0]

        #busco el año de estrno de la pelicula
        movieYear=dfMoviesDuration.loc[dfMoviesDuration["movie_title"] == Pelicula, ["release_year"]]
        movieYear=movieYear.iloc[0, 0]

        return f"La película {(Pelicula).capitalize()} fue estrenada en el año {movieYear} con una duración de {movieDuration} minutos."
    else:
         return f"ERROR: '{(Pelicula).capitalize()}' no es una película valida. Intente nuevamente."



#-------------------------------------------------------------------------------------------------------#
######################################## TERCERA FUINCION ###############################################
#-------------------------------------------------------------------------------------------------------#

#def franquicia( Franquicia: str ): Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
#    Ejemplo de retorno: La franquicia X posee X peliculas, una ganancia total de x y una ganancia promedio de xx

@app.get("/movies/franquicia/{Franquicia}") #decorator
def franquicia( Franquicia: str ):
    dfFranquicia = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfFranquicia.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfFranquicia.append(row)

    #transformo resultado en df
    dfFranquicia=pd.DataFrame(dfFranquicia)

    #cambio a lowercase para que no hayan errores de capitalizacion en el input de mi funcion
    dfFranquicia["franquicia"] = dfFranquicia["franquicia"].str.lower()
    Franquicia = Franquicia.lower()

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    franquicias = set([i for i in dfFranquicia.franquicia])
        
    if Franquicia in franquicias:

        cantidadPeliculas = dfFranquicia.loc[dfFranquicia["franquicia"] == Franquicia, ["movie_count"]]
        cantidadPeliculas = cantidadPeliculas.iloc[0, 0]

        ganancia = dfFranquicia.loc[dfFranquicia["franquicia"] == Franquicia, ["ganancia_total"]]
        ganancia = ganancia.iloc[0, 0]

        ganancia_promedio = dfFranquicia.loc[dfFranquicia["franquicia"] == Franquicia, ["ganancia_promedio"]]
        ganancia_promedio= ganancia_promedio.iloc[0, 0]

        return f"La franquicia {(Franquicia).capitalize} posee {cantidadPeliculas} películas, una ganancia total de {ganancia} y una ganancia promedio de {ganancia_promedio}."

    else:
         
         return f"ERROR: '{(Franquicia).capitalize()}' no es una franquicia valida. Intente nuevamente."
print(franquicia("Toy Story Collection"))