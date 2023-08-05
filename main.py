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

#FOR WHATEVER REASON THE FUNCTION CANT FIND ANY MOVIE, LETS CONTINUE TOMORROW



