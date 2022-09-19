from small_movies.small_movies_dataset import small_dataset
from pickle_file_loader.pickle_files import pickle_files_data as pfd

class collab:

    def get_estimated_val(user,movies):
        # import svd model
        svd = pfd.svd()

        # import indices map
        indices_map = pfd.indices_map()
        movies['estimated_val'] = movies['id'].apply(lambda x:
                                                     svd.predict(user, indices_map.loc[x]['movieId']).est)
        movies = movies.sort_values('estimated_val', ascending=False).head(5)
        return movies

    def get_collab_recommend(user):
        # gets list of not watched movies by user
        nw_movies = small_dataset.get_not_watched_movies(user)

        movies =collab.get_estimated_val(user,nw_movies)
        # c_movies displays recommendations which the user has not yet watched
        return movies
