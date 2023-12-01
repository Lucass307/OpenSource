import os
import unittest
from unittest.mock import patch
from io import StringIO  # Importez StringIO depuis le module io

def ls(directory="."):
    if os.path.exists(directory):
        files = os.listdir(directory)

        for file in files:
            print(file)
    else:
        print(f"Directory '{directory}' does not exist.")

class TestLSFunction(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_ls_custom_directory(self, mock_stdout):
        # Appeler la fonction ls avec un répertoire spécifique
        custom_directory = os.path.join("C:", "Users", "Lucas")
        ls(custom_directory)

        # Récupérer la sortie
        output = mock_stdout.getvalue().strip()

        # Vérifier si la sortie n'est pas vide
        self.assertTrue(output, "No output from ls function.")

if __name__ == "__main__":
    unittest.main()
