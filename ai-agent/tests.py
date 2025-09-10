import unittest
from functions.get_files_info import get_files_info


class TestFunctions(unittest.TestCase):
    def test_calculator_dir(self):
        result = get_files_info("calculator", ".")
        self.assertTrue("Result for current directory:" in result)
        self.assertTrue("- main.py: file_size=576 bytes, is_dir=False" in result)
        self.assertTrue("- tests.py: file_size=1343 bytes, is_dir=False" in result)
        self.assertTrue("- pkg: file_size=2507 bytes, is_dir=True" in result)

    def test_calculator_pkg_dir(self):
        result = get_files_info("calculator", "pkg")
        self.assertTrue("Result for current directory:" in result)
        self.assertTrue("- calculator.py: file_size=1739 bytes, is_dir=False" in result)
        self.assertTrue("- render.py: file_size=768 bytes, is_dir=False" in result)


if __name__ == "__main__":
    unittest.main()
