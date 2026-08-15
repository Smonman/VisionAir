import string
import unittest

import VisionAir as va


class TestEncryption(unittest.TestCase):
    def test_encryption(self):
        alphabet = va.Alphabet(list(string.ascii_uppercase))
        table = va.EncryptionVigenereTable(alphabet)
        result = list(va.encrypt("test", "code", table))
        self.assertEqual(["V", "S", "V", "X"], result)

    def test_encryption_with_key(self):
        alphabet = va.new_keyed_alphabet(list(string.ascii_uppercase), list("key"))
        table = va.EncryptionVigenereTable(alphabet)
        result = list(va.encrypt("test", "code", table))
        self.assertEqual(["Z", "P", "Z", "U"], result)

    def test_encryption_decryption(self):
        alphabet = va.Alphabet(list(string.ascii_uppercase))
        encryption_table, decryption_table = va.get_tables(alphabet)
        text = list("test")
        code = "code"
        encrypted = list(va.encrypt(text, code, encryption_table))
        decrypted = list(va.decrypt(encrypted, code, decryption_table))
        self.assertEqual(
            list(map(lambda c: c.upper(), text)),
            list(map(lambda c: c.upper(), decrypted)),
        )


if __name__ == "__main__":
    unittest.main()
