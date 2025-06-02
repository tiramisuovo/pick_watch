import requests
from models import Movie, Anime
from api_key import api_key
API_KEY = api_key # Please enter your own TMDB api key as a string here :)

def obtain_movie(title):
    """ obtain a movie from TMDB and create a movie object"""
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key={API_KEY}"

    response = requests.get(url)
    movie_data = response.json()

    if not movie_data['results']:
        return None

    first_result = movie_data['results'][0]
    movie_title = first_result['title']
    movie_release = first_result.get('release_date',"unknown")
    movie_overview = first_result.get('overview',"unknown")
    movie_poster = first_result.get('poster_path', "")
    
    return Movie(movie_title, movie_release, movie_overview, movie_poster)

def obtain_movie_poster(poster_path):
    if poster_path:
        url_poster = f"https://image.tmdb.org/t/p/w500{poster_path}"
        response_poster = requests.get(url_poster)
        if response_poster.status_code == 200:
            movie_poster = response_poster.content
            return movie_poster
        return None

def obtain_anime(title):
    """ obtain an anime from Jikan and create a anime object"""
    url = f"https://api.jikan.moe/v4/anime?q={title}&limit=1"

    response = requests.get(url)
    anime_data = response.json()

    if not anime_data["data"]:
        return None
    
    first_result = anime_data["data"][0]
    anime_title = first_result["title"]
    release_time = first_result["aired"].get("from","unknown")
    anime_release = release_time[:10]
    anime_overview = first_result.get("synopsis","unknown")
    anime_poster = first_result["images"]["jpg"].get("image_url","")

    return Anime(anime_title, anime_release, anime_overview, anime_poster)

def obtain_anime_poster(poster_url):
    if poster_url:
        response_poster = requests.get(poster_url)
        if response_poster.status_code == 200:
            anime_poster = response_poster.content
            return anime_poster
        return None
