import streamlit as st
from background.bkg_image import bkg_image
from movie_details.details import movie_details
from display.show_recommendations import show
from recommendations.recommendations_collab import collab


# background image
bkg = bkg_image
bkg.add_bg_from_local('image/image.jpg')


st.title('Movie Recommender System')

user = st.number_input('Enter User Id and click on recommend to know the recommendations',min_value=1,max_value=671)

if st.button('Recommend'):
    df = collab.get_collab_recommend(user)

    #Use top 5 recommendations
    df=df.head(5)

    st.caption('Collaborative Recommendations Based on your past Ratings and Ratings '
               'of other similar users')

    movie_details.get_details(df)
