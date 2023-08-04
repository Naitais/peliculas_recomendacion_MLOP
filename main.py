from fastapi import FastAPI
import csv

app = FastAPI()



@app.get("/")
def home():
    return {"HOME": "puto el que lee"}


def load_movies():
    movies = []
    with open(r"datasets\datasets_limpios\dfMovies.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append(row)
        return movies
    
@app.get("/movies/first-row")
def get_first_row():
    movies = load_movies()
    first_row = movies[0] if movies else None
    return first_row