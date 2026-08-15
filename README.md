# VisionAir

_A simple [Vigenere-Chiffre](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) program_

Encrypts and decrypts text using a [Vigenere-Chiffre](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). No AI was
used in the making of this program.

## Synopsis

```
main.py [-h] [-a ALPHABET] [-k ALPHABET_KEY] -c CODE [-v] [-d] {encrypt,decrypt} [input_file]
```

### Positional Arguments

| Argument     | Possible Values                                        | Description                     |
|--------------|--------------------------------------------------------|---------------------------------|
| `mode`       | `encrypt`, `decrypt`                                   | The mode of the program         |
| `input_file` | either a path to a file, or nothing to read from STDIN | The file to be en- or decrypted |

### Options

| Option                 | Possible Values                                                                                             | Description                              |
|------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------|
| `-h`, `--help`         |                                                                                                             | show this help message and exit          |
| `-a`, `--alphabet`     | Either a custom alphabet as as string, or the keywords `english` or `german` for their respective alphabet. | The alphabet used for the Vigenere-Table |
| `-k`, `--alphabet-key` | String                                                                                                      | The key for the Vigenere-Table           |
| `-c`, `--code`         | String                                                                                                      | The code for the en- and decryption      |
| `-v`, `--verbose`      |                                                                                                             | Show more log output                     |
| `-d`, `--debug`        |                                                                                                             | Show debug log messages                  |

### Examples

```PowerShell
> "test" | python main.py encrypt --code code
VSVX
```

```PowerShell
> "VSVX" | python main.py decrypt --code code
TEST
```

## API Example

```python
import VisionAir as va

chiffre = va.VigenereChiffre.from_keyed_alphabet("abcdefghijklmnopqrstuvwxyz", "key")

encrypted_generator = chiffre.encrypt("plaintext", "code")
decrypted_generator = chiffre.decrypt(encrypted_generator, "code")

plaintext = "".join(decrypted_generator)  # consume generator to string
```

## Limitations

- Currently, unsupported characters are simply skipped. Other techniques to handle such cases could be explored, e.g.
  stripping them.
- Limited unit testing
- No proper documentation
- Could be extended to a Python Project