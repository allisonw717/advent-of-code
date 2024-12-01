import os

def set_file_reader():
    path = os.path.realpath(__file__) 
    dir = os.path.dirname(path) 
    dir = dir.replace('src', 'inputs') 
    os.chdir(dir) 
