import unittest
from scripts.sdlc_validator import validate_file_exists, validate_version_format

class TestSDLCValidator(unittest.TestCase):
    def test_validate_file_exists(self):
        self.assertTrue(validate_file_exists("README.md"))
        self.assertFalse(validate_file_exists("nonexistent_file.md"))

    def test_validate_version_format(self):
        with open("version.txt", "w") as f:
            f.write("v1.0.0")
        self.assertTrue(validate_version_format())
        with open("version.txt", "w") as f:
            f.write("invalid_version")
        self.assertFalse(validate_version_format())

if __name__ == "__main__":
    unittest.main()