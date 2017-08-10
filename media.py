import webbrowser
import urllib
import json
import os

# user needs to obtain APIs for The Movie Database and Youtube
# and save as environmental variables
YOUTUBE_API =(os.environ['YOUTUBE_API'])
TMDB_API = (os.environ['TMDB_API'])

class Movie():
    def __init__(self, movie_title):
        self.title = movie_title
        # call up tmdb api to load poster and overview for each movie
        tmdb_connection = urllib.urlopen("https://api.themoviedb.org/3/search/movie?api_key="+TMDB_API+"&query="+movie_title)  # NOQA
        tmdb_json_data = tmdb_connection.read()
        tmdb_results = (json.loads(tmdb_json_data))
        self.summary = tmdb_results["results"][0]["overview"]
        self.poster_image_url = "https://image.tmdb.org/t/p/w640"+tmdb_results["results"][0]["poster_path"]  # NOQA
        # call up youtube API to search for a trailer for each movie
        youtube_connection = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&q="+movie_title+"official%20trailer&maxResults=5&key="+YOUTUBE_API)  # NOQA
        youtube_json_data = youtube_connection.read()
        youtube_results = (json.loads(youtube_json_data))
        self.trailer_youtube_url = "https://www.youtube.com/watch?v="+youtube_results["items"][0]["id"]["videoId"]  # NOQA
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    
