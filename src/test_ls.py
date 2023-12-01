# test_ls_function.py
import unittest
from unittest.mock import patch
from io import StringIO
from ls import ls  # Importez la fonction ls depuis votre module principal

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
