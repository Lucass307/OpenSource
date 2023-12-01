import os

def ls(directory="."):
    files = os.listdir(directory)

    for file in files:
        print(file)

ls()