import streamlit as st
from background.bkg_image import bkg_image
from movie_details.details import movie_details
from display.show_recommendations import show
from recommendations.recommendations_content import content
from pickle_file_loader.pickle_files import pickle_files_data as pfd

# background image
bkg = bkg_image
bkg.add_bg_from_local('image/image.jpg')

st.title('Movie Recommender System')

# loads the titles to display
titles = pfd.titles()

movie_name = st.selectbox(
    'Select movie name and click on recommend to know the recommendations based on content', titles.values)

if st.button('Recommend'):
    df = content.get_recommend_content(movie_name)

    # Use top 5 recommendations
    df = df.head(5)
    st.caption('Content Based Recommendations')
    movie_details.get_details(df)
