import os

def get_main_directory():
    return os.path.dirname(os.path.abspath(__file__))

def construct_full_path(directory, filename):
    return os.path.join(directory, filename)
