import unittest
from app import hello_dev, welcome_message


class TestHelloWorld(unittest.TestCase):

    # Test 1: Verify the hello_dev message
    def test_hello_world_message(self):
        self.assertEqual(
            hello_dev(),
            "Hello, Anmol!"
        )

    # Test 2: Verify the return type
    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_dev(), str)

    # Test 3: Test welcome_message with Anmol
    def test_welcome_message_anmol(self):
        self.assertEqual(
            welcome_message("Anmol"),
            "Welcome to DevOps, Anmol!"
        )

    # Test 4: Test welcome_message with Rahul
    def test_welcome_message_rahul(self):
        self.assertEqual(
            welcome_message("Rahul"),
            "Welcome to DevOps, Rahul!"
        )


if __name__ == "__main__":
    unittest.main()
