import unittest
from app import hello_dev


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(
            hello_dev(),
            "Hello, DevOps!"
        )
        
    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_dev(), str)


if __name__ == "__main__":
    unittest.main()
