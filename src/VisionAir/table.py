import logging
from abc import ABC, abstractmethod

import VisionAir as va

LOGGER = logging.getLogger()


class VigenereTable(ABC):
    def __init__(self, alphabet: va.Alphabet):
        self.alphabet = alphabet

    def __contains__(self, letter: str) -> bool:
        return letter in self.alphabet

    def __getitem__(self, index: tuple[str, str]) -> str:
        return self.get(index)

    def __str__(self):
        return str(self.alphabet)

    def _letter_to_index(self, letter: str) -> int:
        return list(self.alphabet).index(letter.upper())

    @abstractmethod
    def get(self, index: tuple[str, str]) -> str:
        pass

    def pretty_print(self) -> str:
        result = ""
        result += " " * 7
        for letter_col in self.alphabet:
            result += f"{self._letter_to_index(letter_col):<2} "
        result += "\n"
        result += " " * 7
        for letter_col in self.alphabet:
            result += f"{letter_col:<2} "
        result += "\n"
        result += " " * 7
        result += "-" * len(self.alphabet) * 3
        result += "\n"
        for letter_row in self.alphabet:
            result += f"{self._letter_to_index(letter_row):2} {letter_row:1} | "
            for letter_col in self.alphabet:
                result += f"{self[(letter_row, letter_col)]:<2} "
            result += "\n"
        return result


class EncryptionVigenereTable(VigenereTable):
    def get(self, index: tuple[str, str]) -> str:
        index_row = self._letter_to_index(index[0])
        index_col = self._letter_to_index(index[1])
        index_result = (index_row + index_col) % len(self.alphabet)
        return self.alphabet[index_result]


class DecryptionVigenereTable(VigenereTable):
    def get(self, index: tuple[str, str]) -> str:
        index_row = self._letter_to_index(index[0])
        index_col = self._letter_to_index(index[1])
        index_result = (index_row - index_col) % len(self.alphabet)
        return self.alphabet[index_result]


def get_tables(
    alphabet: va.Alphabet,
) -> tuple[EncryptionVigenereTable, DecryptionVigenereTable]:
    return va.EncryptionVigenereTable(alphabet), va.DecryptionVigenereTable(alphabet)
