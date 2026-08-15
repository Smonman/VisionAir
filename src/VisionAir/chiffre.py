from typing import Self, Generator, Iterable

import VisionAir as va


class VigenereChiffre:
    def __init__(self, alphabet: va.Alphabet):
        self.alphabet = alphabet
        self._encryption_table, self._decryption_table = va.get_tables(alphabet)

    @classmethod
    def from_raw_alphabet(cls, alphabet: str) -> Self:
        return cls(va.Alphabet(list(alphabet)))

    @classmethod
    def from_keyed_alphabet(cls, alphabet: str, key: str) -> Self:
        return cls(va.new_keyed_alphabet(list(alphabet), list(key)))

    @property
    def encryption_table(self) -> va.EncryptionVigenereTable:
        return self._encryption_table

    @property
    def decryption_table(self) -> va.DecryptionVigenereTable:
        return self._decryption_table

    def encrypt(self, text: Iterable[str], code: str) -> Generator[str]:
        return va.encrypt(text, code, self._encryption_table)

    def decrypt(self, text: Iterable[str], code: str) -> Generator[str]:
        return va.decrypt(text, code, self._decryption_table)
