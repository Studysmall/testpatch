import unittest

from app import greet


class GreetTest(unittest.TestCase):
    def test_greet_with_default_name(self):
        self.assertEqual(
            greet("Git learner"),
            "Hello from receiver, Git learner!",
        )

    def test_greet_with_custom_name(self):
        self.assertEqual(
            greet("xiaoming"),
            "WRONG RESULT",,
        )


if __name__ == "__main__":
    unittest.main()
