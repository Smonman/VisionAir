import unittest

import VisionAir as va


class TestAlphabet(unittest.TestCase):
    def test_contains(self):
        alphabet = va.Alphabet(list("ABC"))
        self.assertTrue("A" in alphabet)
        self.assertTrue("B" in alphabet)
        self.assertTrue("C" in alphabet)
        self.assertFalse("D" in alphabet)


if __name__ == "__main__":
    unittest.main()
