import logging
from typing import Generator, Iterable

import VisionAir as va

LOGGER = logging.getLogger()


def _get_code_stream_at(code: str, index: int) -> str:
    return code[index % len(code)]


def encrypt(
    plaintext: Iterable[str], code: str, table: va.EncryptionVigenereTable
) -> Generator[str]:
    LOGGER.debug("encrypting...")
    return _look_up_table(plaintext, code, table)


def decrypt(
    ciphertext: Iterable[str], code: str, table: va.DecryptionVigenereTable
) -> Generator[str]:
    LOGGER.debug("decrypting...")
    return _look_up_table(ciphertext, code, table)


def _look_up_table(
    text: Iterable[str], code: str, table: va.VigenereTable
) -> Generator[str]:
    for i, c in enumerate(text):
        if c not in table:
            LOGGER.info(f"letter {ascii(c)} ({hex(ord(c))}) cannot be found, ignoring")
            yield c
        else:
            code_c = _get_code_stream_at(code, i)
            if code_c not in table:
                raise ValueError(
                    f"letter {ascii(code_c)} ({hex(ord(code_c))}) from code '{code}' cannot be found in the table"
                )
            yield table.get((c, code_c))
