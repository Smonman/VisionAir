import argparse
import fileinput
import itertools
import logging.config
import pathlib
import string

import VisionAir as va

logging.config.fileConfig("resources/logging.conf")
LOGGER = logging.getLogger()


def setup_logger(args: argparse.Namespace) -> None:
    if args.verbose:
        LOGGER.setLevel(logging.INFO)
    if args.debug:
        LOGGER.setLevel(logging.DEBUG)


def main(args: argparse.Namespace) -> None:
    LOGGER.debug(args)
    chiffre = va.VigenereChiffre.from_keyed_alphabet(
        get_raw_alphabet(args.alphabet), args.alphabet_key
    )
    LOGGER.debug("encryption table:\n" + chiffre.encryption_table.pretty_print())
    LOGGER.debug("decryption table:\n" + chiffre.decryption_table.pretty_print())
    with fileinput.input(files=args.input_file, encoding="utf-8") as file:
        letters = itertools.chain.from_iterable(file)
        if args.mode == "encrypt":
            result_generator = chiffre.encrypt(letters, args.code)
        else:
            result_generator = chiffre.decrypt(letters, args.code)
        result = "".join(result_generator)
    print(result, end="")


def get_raw_alphabet(name_or_characters: str) -> str:
    LOGGER.debug(f"getting raw alphabet: {name_or_characters}")
    if name_or_characters.lower() == "english":
        LOGGER.info(f"interpreting '{name_or_characters}' as english alphabet")
        return string.ascii_uppercase
    elif name_or_characters.lower() == "german":
        LOGGER.info(f"interpreting '{name_or_characters}' as german alphabet")
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜẞ"
    else:
        LOGGER.info(f"creating new alphabet with letters '{name_or_characters}'")
        return name_or_characters.upper()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", type=str, choices=["encrypt", "decrypt"], default="encrypt"
    )
    parser.add_argument(
        "-a",
        "--alphabet",
        type=str,
        default="english",
        help="The alphabet used for the Vigenere-Table",
    )
    parser.add_argument(
        "-k",
        "--alphabet-key",
        type=str,
        default="",
        required=False,
        help="The key for the Vigenere-Table",
    )
    parser.add_argument(
        "-c",
        "--code",
        type=str,
        required=True,
        help="The code for the en- and decryption",
    )
    parser.add_argument(
        "input_file",
        type=pathlib.Path,
        default="-",
        nargs="?",
        help="The file to be en- or decrypted",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        help="show more log output",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="show debug log messages",
    )
    parsed_args = parser.parse_args()
    setup_logger(parsed_args)
    main(parsed_args)
