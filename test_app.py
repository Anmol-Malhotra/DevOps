import unittest
from app import hello_dev, welcome_message


class TestHelloDev(unittest.TestCase):

    # Test 1: Verify hello_dev message
    def test_hello_dev_message(self):
        self.assertEqual(
            hello_dev(),
            "Hello, DevOps!"
        )

    # Test 2: Verify return type
    def test_hello_dev_type(self):
        self.assertIsInstance(
            hello_dev(),
            str
        )

    # Test 3: Test welcome message for Anmol
    def test_welcome_message_anmol(self):
        self.assertEqual(
            welcome_message("Anmol"),
            "Welcome to DevOps, Anmol!"
        )

    # Test 4: Test welcome message for Rohan
    def test_welcome_message_rohan(self):
        self.assertEqual(
            welcome_message("Rohan"),
            "Welcome to DevOps, Rohan!"
        )


if __name__ == "__main__":
    unittest.main()
