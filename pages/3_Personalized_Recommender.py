import streamlit as st
from background.bkg_image import bkg_image
from movie_details.details import movie_details
from display.show_recommendations import show
from recommendations.recommendations_hybrid import hybrid
from pickle_file_loader.pickle_files import pickle_files_data as pfd

bkg=bkg_image
bkg.add_bg_from_local('image/image.jpg')

st.title('Movie Recommender System')

# loads the titles to display
titles = pfd.titles()

user = st.number_input('Enter User Id ',min_value=1,max_value=671)
movie_name = st.selectbox(
    'Select movie name', titles.values)

if st.button('Recommend'):
    df = hybrid.get_hybrid_recommend(movie_name,user)

    # Use top 5 recommendations
    df = df.head(5)
    st.caption(
        'Personalized Recommendations based on your past Ratings, Ratings of other similar users and content of the movies')

    movie_details.get_details(df)
