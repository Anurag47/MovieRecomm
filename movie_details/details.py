from poster_details.poster_details import poster
from display.show_recommendations import show
class movie_details:

    def get_details(df):

        movie_list = []
        movie_poster = []
        length = len(df)

        for i in range(length):
            m_name = df.iloc[i].title
            m_id = df.iloc[i].id

            m_poster = poster.fetch_poster(m_id)

            movie_list.append(m_name)
            movie_poster.append(m_poster)

        show.show_details(movie_list, movie_poster)