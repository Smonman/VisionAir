import collections
import logging
import string

LOGGER = logging.getLogger()


class Alphabet:
    def __init__(self, letters: list[str]):
        for k, v in collections.Counter(letters).items():
            if v > 1:
                raise ValueError(
                    f"Alphabet can only contain unique letters but '{k}' is contained '{v}' times"
                )
        for l in string.ascii_uppercase:
            if l not in letters:
                LOGGER.warning(
                    f"letter '{l}' of the standard ASCII alphabet is not present in the given alphabet"
                )
        self.content = list(map(lambda c: c.upper(), letters))

    def get(self, index: int) -> str:
        return self.content[index]

    def __getitem__(self, index: int) -> str:
        return self.get(index)

    def __iter__(self):
        return iter(self.content)

    def __len__(self):
        return len(self.content)

    def __contains__(self, item: str):
        return item.upper() in self.content

    def __str__(self):
        return str(self.content)


def new_keyed_alphabet(alphabet: list[str], key: list[str]) -> Alphabet:
    for k, v in collections.Counter(key).items():
        if v > 1:
            raise ValueError(
                f"key can only contain unique letters but '{k}' is contained '{v}' times"
            )
    working_key = list(map(lambda c: c.upper(), key))
    working_alphabet = list(map(lambda c: c.upper(), alphabet))
    keyed_alphabet = working_key + list(
        filter(lambda c: c not in working_key, working_alphabet)
    )
    return Alphabet(keyed_alphabet)
