import unittest
from app import hello_dev


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(
            hello_dev(),
            "Hello, DevOps!"
        )


if __name__ == "__main__":
    unittest.main()
