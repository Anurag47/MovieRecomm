from movie_details.movie_index import movie_index
from small_movies.small_movies_dataset import small_dataset
from weighted_func.weighted import weighted
from pickle_file_loader.pickle_files import pickle_files_data as pfd

class content:

    def get_similar_content(title):

        # loading the dataframe

        similar = pfd.similar()

        ind = movie_index.get_index(title)
        dist_list = list(enumerate(similar[ind]))
        dist_list = sorted(dist_list, key=lambda x: x[1], reverse=True)
        dist_list = dist_list[1:30]
        movie_indices = [i[0] for i in dist_list]
        #fetches the small_movies dataset of the given indices
        similar_movies=small_dataset.get_sm_data_indices(movie_indices)
        return similar_movies
    
    def get_recommend_content(title):

        similar_movies= content.get_similar_content(title)
        C = similar_movies['vote_average'].mean()
        # relaxing the vote count as we have only 30 movies and some movies may not be voted that much
        m = similar_movies['vote_count'].quantile(0.75)
        new_similar = similar_movies[similar_movies['vote_count'] > m]
        new_similar['rating'] = new_similar.apply(lambda x: weighted.get_rating(x, C, m), axis=1)
        new_similar = new_similar.sort_values('rating', ascending=False).head(10)

        return new_similar