# test_ls_function.py
import unittest
from ls import ls

class TestLSFunction(unittest.TestCase):
    def test_ls_default_directory(self):
        # Test la fonction ls avec le répertoire par défaut
        with self.assertOutput(match=".*", msg="No output from ls function."):
            ls()

    def test_ls_custom_directory(self):
        # Test la fonction ls avec un répertoire spécifique
        custom_directory = "/chemin/vers/un/autre/repertoire"
        with self.assertOutput(match=".*", msg="No output from ls function."):
            ls(custom_directory)

if __name__ == "__main__":
    unittest.main()
