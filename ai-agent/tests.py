import unittest
from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content


class TestFunctions(unittest.TestCase):
    def test_calculator_dir(self):
        result = get_files_info("calculator", ".")
        self.assertTrue("Result for current directory:" in result)
        self.assertTrue("- main.py: file_size=576 bytes, is_dir=False" in result)
        self.assertTrue("- tests.py: file_size=1343 bytes, is_dir=False" in result)
        self.assertTrue("- pkg: file_size=2507 bytes, is_dir=True" in result)

    def test_calculator_pkg_dir(self):
        result = get_files_info("calculator", "pkg")
        self.assertTrue("Result for 'pkg' directory:" in result)
        self.assertTrue("- calculator.py: file_size=1739 bytes, is_dir=False" in result)
        self.assertTrue("- render.py: file_size=768 bytes, is_dir=False" in result)

    def test_calculator_bin_dir(self):
        result = get_files_info("calculator", "/bin")
        self.assertTrue("Error: cannot list" in result)

    def test_calculator_main_file(self):
        result = get_file_content("calculator", "main.py")
        self.assertTrue("Result for current directory:" in result)
        self.assertTrue("- main.py: file_size=576 bytes, is_dir=False" in result)
        self.assertTrue("- tests.py: file_size=1343 bytes, is_dir=False" in result)
        self.assertTrue("- pkg: file_size=2507 bytes, is_dir=True" in result)

    def test_calculator_pkg_calculator_file(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertTrue("Result for 'pkg' directory:" in result)
        self.assertTrue("- calculator.py: file_size=1739 bytes, is_dir=False" in result)
        self.assertTrue("- render.py: file_size=768 bytes, is_dir=False" in result)

    def test_calculator_bin_cat(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertTrue("Error: file not found" in result)

    def test_calculator_does_not_exist_file(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertTrue("Error: file not found" in result)


if __name__ == "__main__":
    unittest.main()
