# tests/test_main.py

import unittest
import subprocess
from src.main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

    def test_main_execution(self):
        # Run the script and capture the output
        result = subprocess.run(['python', 'src/main.py'], capture_output=True, text=True)
        
        # Check that the output is as expected
        self.assertEqual(result.stdout.strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
