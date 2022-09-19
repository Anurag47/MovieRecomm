from recommendations.recommendations_content import content
from recommendations.recommendations_collab import collab

class hybrid:

    def get_hybrid_recommend(movie_name,user):
        #gets a df of similar movies
        similar_movies= content.get_similar_content(movie_name)

        similar_movies =similar_movies[['title', 'vote_count', 'vote_average', 'id']]

        movies=collab.get_estimated_val(user,similar_movies)
        return movies