import requests

class poster:
    def fetch_poster(movie_id):
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=c319518b6dc4599bd882d63ecbcf7e6a&language=en-US'.format(
                movie_id))
        data = response.json()
        poster_path= "https://image.tmdb.org/t/p/w500" + data['poster_path']
        return poster_path

