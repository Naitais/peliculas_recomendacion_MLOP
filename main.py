from fastapi import FastAPI
import csv , pandas as pd


app = FastAPI()

@app.get("/")
def home():
    return {"HOME": "home"}

#----------------------------------------------- PRIMERA FUINCION -----------------------------------------------------#


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
        return f"La cantidad de películas estrenadas en idioma '{(Idioma).title()}' es {cantidadPels}."
    else: 
        return f"ERROR: '{(Idioma).title()}' no es un idioma valido o no hay información disponible. Ejemplo de idioma valido: en, es, fr, etc. Intente nuevamente."


#----------------------------------------------- SEGUNDA FUINCION -----------------------------------------------------#


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
    dfMoviesDuration["movie_title"] = dfMoviesDuration["movie_title"].str.lower().str.strip()
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

        return f"La película {(Pelicula).title()} fue estrenada en el año {movieYear} con una duración de {movieDuration} minutos."
    else:
         return f"ERROR: '{(Pelicula).title()}' no es una película valida o no hay información disponible. Intente nuevamente."


#----------------------------------------------- TERCERA FUINCION -----------------------------------------------------#


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
    dfFranquicia["franquicia"] = dfFranquicia["franquicia"].str.lower().str.strip()
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

        return f"La franquicia {(Franquicia).title()} posee {cantidadPeliculas} películas, una ganancia total de {ganancia} y una ganancia promedio de {ganancia_promedio}."

    else:
         
         return f"ERROR: '{(Franquicia).title()}' no es una franquicia valida o no hay información disponible. Intente nuevamente."


#----------------------------------------------- CUARTA FUINCION -----------------------------------------------------#

#def peliculas_pais( Pais: str ): Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
#    Ejemplo de retorno: Se produjeron X películas en el país X

@app.get("/movies/pais/{Pais}") #decorator
def peliculas_pais( Pais: str ):
    dfPaises = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfPaises.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfPaises.append(row)

    #transformo resultado en df
    dfPaises=pd.DataFrame(dfPaises)

    #cambio a lowercase para que no hayan errores de capitalizacion en el input de mi funcion
    dfPaises["production_country"] = dfPaises["production_country"].str.lower().str.strip()
    Pais = Pais.lower()

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    paises=set([i for i in dfPaises["production_country"]])
        
    if Pais in paises:

        cantidadPeliculas = dfPaises.loc[(dfPaises["production_country"]==Pais),["movie_count"]]
        cantidadPeliculas=cantidadPeliculas.iloc[0, 0]
        return f"En {(Pais).title()} se produjeron {cantidadPeliculas} películas."

    else:
         
         return f"ERROR: '{(Pais).title()}' no es un país valido o no hay información disponible. Intente nuevamente."


#----------------------------------------------- QUINTA FUINCION -----------------------------------------------------#

@app.get("/movies/productora/{Productora}") #decorator
def productoras_exitosas( Productora: str ):
    dfProductora = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfProductora.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfProductora.append(row)

    #transformo resultado en df
    dfProductora=pd.DataFrame(dfProductora)

    #cambio a lowercase para que no hayan errores de capitalizacion en el input de mi funcion
    dfProductora["production_company"] = dfProductora["production_company"].str.lower().str.strip()
    Productora = Productora.lower()

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    productoras = set([i for i in dfProductora.production_company])
        
    if Productora in productoras:

        cantidadPeliculas = dfProductora.loc[dfProductora["production_company"] == Productora, ["movie_count"]]
        cantidadPeliculas = cantidadPeliculas.iloc[0, 0]

        ganancia = dfProductora.loc[dfProductora["production_company"] == Productora, ["ganancia_total"]]
        ganancia = ganancia.iloc[0, 0]

        return f"La productora {(Productora).title()} posee {cantidadPeliculas} películas y una ganancia total de {ganancia}."

    else:
         
         return f"ERROR: '{(Productora).title()}' no es una productora valida o no hay información disponible. Intente nuevamente."



#----------------------------------------------- SEXTA FUINCION -----------------------------------------------------#

#def get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un 
# dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el 
# nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.

@app.get("/movies/info_directores/{nombre_director}") #decorator
def get_director( nombre_director ):
    #PRIMER DATASET DIRECTORES EXITO
    dfDirectoresExito = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfDirectoresExito.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfDirectoresExito.append(row)

    #transformo resultado en df
    dfDirectoresExito=pd.DataFrame(dfDirectoresExito)

    #SEGUNDO DATASET DIRECOTRES INFO PELICULA
    dfDirectoresInfoPeliculas = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(r"datasets\datasets_limpios\dfDirectoresInfoPeliculas.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dfDirectoresInfoPeliculas.append(row)

    #transformo resultado en df
    dfDirectoresInfoPeliculas=pd.DataFrame(dfDirectoresInfoPeliculas)

    #cambio a lowercase para que no hayan errores de capitalizacion en el input de mi funcion
    #Tambien le hago un strip para que quite espacios de mas porque algunos nombres no los encontraba
    dfDirectoresExito["name"] = dfDirectoresExito["name"].str.lower().str.strip()
    dfDirectoresInfoPeliculas["name"] = dfDirectoresInfoPeliculas["name"].str.lower().str.strip()
    nombre_director = nombre_director.lower()

    #busco todos los idiomas. Usando la funcion set, me trae valores unicos
    directores = set([i for i in dfDirectoresExito.name])

        
    if nombre_director in directores:

        exito = dfDirectoresExito.loc[dfDirectoresExito["name"] == nombre_director, ["director_return"]]
        exito = exito.iloc[0, 0]

        infoPelicula = dfDirectoresInfoPeliculas[dfDirectoresInfoPeliculas["name"] == nombre_director]

        listaDictPeliculas= [] #meto en una lista diccionarios con la info de cada pelicula del director
        for i in range(len(infoPelicula)):
            row=infoPelicula.iloc[i].to_dict() #si uso la funcion to_dict() transformo cada row en un diccionario
            listaDictPeliculas.append(row)
        exitoMensaje=f"El director {(nombre_director).title()} posee un exito medido por el retorno de {exito}. A continuación se lista información de sus películas:"

        for key in listaDictPeliculas: #remuevo key/value pairs que son innecesarios en el diccionario
            key.pop("", None)
            key.pop("name", None)

        return exitoMensaje,  listaDictPeliculas #al retornar cada variable por separado, python mete a ambas en una tupla

    else:
         
         return f"ERROR: '{(nombre_director).title()}' no es un nombre de director valido o no hay información disponible. Intente nuevamente."
from fastapi import FastAPI
import csv , locale, pandas as pd

import pandas
import fastapi
print("fastapi",fastapi.__version__)
print("csv",csv.__version__)
print("pandas",pandas.__version__)
print("locale",locale.__version__)