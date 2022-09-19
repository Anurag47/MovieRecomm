import streamlit as st
from background.bkg_image import bkg_image
from genre.genre_based import top_movies_genre
from movie_details.details import movie_details

from pickle_file_loader.pickle_files import pickle_files_data as pfd

# background image
bkg=bkg_image
bkg.add_bg_from_local('image/image.jpg')


st.title('Movie Recommender System')

genre = st.selectbox(
    'Select genre and click on recommend',
    ('Action', 'Thriller', 'Adventure', 'Comedy', 'Science Fiction', 'Fantasy', 'Crime', 'Drama', 'Romance',
     'Animation', 'Horror'))



if st.button('Recommend'):
    gen_df = top_movies_genre.build_chart(genre)
    st.caption('Top Rated movies in the selected genre ')
    movie_details.get_details(gen_df.head(10))


    #show.show_details(movie_list, movie_poster)
else:
    featured =pfd.featured()
    st.caption('Top Rated movies')
    movie_details.get_details(featured.head(10))