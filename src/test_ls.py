import os
import unittest
from io import StringIO
import sys

def ls(directory="."):
    files = os.listdir(directory)

    for file in files:
        print(file)

class TestLSFunction(unittest.TestCase):
    def setUp(self):
        # Rediriger la sortie standard vers un StringIO
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

    def test_ls_default_directory(self):
        # Appeler la fonction ls
        ls()

        # Récupérer la sortie
        output = self.held_output.getvalue().strip()

        # Vérifier si la sortie n'est pas vide
        self.assertTrue(output, "No output from ls function.")

    def test_ls_custom_directory(self):
        # Appeler la fonction ls avec un répertoire spécifique
        custom_directory = "C:\\Users\\"
        ls(custom_directory)

        # Récupérer la sortie
        output = self.held_output.getvalue().strip()

        # Vérifier si la sortie n'est pas vide
        self.assertTrue(output, "No output from ls function.")

if __name__ == "__main__":
    unittest.main()
