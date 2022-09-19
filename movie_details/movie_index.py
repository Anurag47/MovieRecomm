from pickle_file_loader.pickle_files import pickle_files_data as pfd
class movie_index:

    def get_index(title):

        indices = pfd.indices()
        ind = indices[title]
        return ind