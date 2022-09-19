import pickle


class pickle_files_data:

    def featured():
        df = pickle.load(open(r'./Pickle_Files/featured.pkl', 'rb'))
        return df

    def indices():
        df = pickle.load(open(r'./Pickle_Files/indices.pkl', 'rb'))
        return df

    def indices_map():
        df = pickle.load(open(r'./Pickle_Files/indices_map.pkl', 'rb'))
        return df

    def similar():
        df = pickle.load(open(r'./Pickle_Files/similar.pkl', 'rb'))
        return df

    def sm_movies():
        df = pickle.load(open(r'./Pickle_Files/sm_movies.pkl', 'rb'))
        return df

    def svd():
        df = pickle.load(open(r'./Pickle_Files/svd.pkl', 'rb'))
        return df

    def tempdf():
        df = pickle.load(open(r'./Pickle_Files/tempdf.pkl', 'rb'))
        return df

    def titles():
        df = pickle.load(open(r'./Pickle_Files/titles.pkl', 'rb'))
        return df
