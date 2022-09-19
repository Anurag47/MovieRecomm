from pickle_file_loader.pickle_files import pickle_files_data as pfd


class top_movies_genre:

    def build_chart(genre):
        featured = pfd.featured()

        genre_values = featured['genres'].apply(lambda x: genre in x)
        genre_df = featured[genre_values]
        return genre_df.head(10)
