import streamlit as st


class show:

    def show_details(movie_list,movie_poster):
        length = len(movie_list)

        ind=0
        for i in range(length//5):
            cols = st.columns(5)
            for j in range(5):
                with cols[j]:
                    st.image(movie_poster[ind])
                    st.caption(movie_list[ind])
                ind=ind+1