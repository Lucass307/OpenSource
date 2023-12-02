import os
import sys

def ls(directory="."):
    if os.path.exists(directory):
        files = os.listdir(directory)
        for file in files:
            print(file)
    else:
        print(f"Directory '{directory}' does not exist.")

# Récupérer les arguments de la ligne de commande
arguments = sys.argv[1:]

# Si des arguments sont fournis, utilisez le premier argument comme emplacement
if arguments:
    ls(arguments[0])
else:
    # Si aucun argument n'est fourni, utilisez le répertoire courant
    ls()
