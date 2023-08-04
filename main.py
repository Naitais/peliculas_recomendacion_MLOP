from fastapi import FastAPI
import csv

app = FastAPI()



@app.get("/")
def home():
    return {"HOME": "puto el que lee"}


def load_movies():
    movies = []
    with open(r"datasets\datasets_limpios\dfMovies.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            movies.append(row)
        return movies
    
@app.get("/movies/")
def get_movie_by_title(title: str):
    movies = load_movies()
    movie = next((m for m in movies if m.get("movie_title", "").lower() == title.lower()), None)
    
    if movie:
        return {
            "title": movie.get("movie_title", ""),
            "genre": movie.get("movie_genre", ""),
            "budget": movie.get("budget", ""),
            "release_year": movie.get("release_year", ""),
            # Add more attributes as needed
        }
