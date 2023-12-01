# ls_function.py
import os


def ls(directory="."):
    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            print(file)
    else:
        print(f"Directory '{directory}' does not exist. Please try again.")
