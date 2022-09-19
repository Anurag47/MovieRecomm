from pickle_file_loader.pickle_files import pickle_files_data as pfd

class small_dataset:

    def get_sm_data_indices(movie_indices):
        sm_movies = pfd.sm_movies()
        similar_movies = sm_movies.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'id']]
        return similar_movies

    def get_not_watched_movies(user):

        sm_movies = pfd.sm_movies()
        tempdf = pfd.tempdf()

        movies = sm_movies[['title', 'vote_count', 'vote_average', 'id']]
        # Checking if the user has already watched the movie or not
        watched_movie = tempdf[tempdf['userId'] == user]['id']
        # removing the movies which have already been watched by the user
        nw_movies = movies[~movies['id'].isin(watched_movie)]
        return nw_movies