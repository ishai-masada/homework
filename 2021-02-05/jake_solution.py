from passlib.hash import pbkdf2_sha1 as sha1
import string
import os
import sys
from typing import Iterable, List, Optional


def clearscreen():
    """ Clears the terminal buffer.
    """
    os.system('clear')


def color(text: str, fg: int = 37, bg: int = 1) -> str:
    """ Surrounds `text` in ANSI color codes.
    """
    return f'\x1b[1;{fg};{bg}m{text}\x1b[0m'


def permutator(characters: Iterable[str]) -> str:
    """ Generates all possible permuations of `characters`.
    """
    attempts = ['']
    while True:
        new_attempts = list()
        for attempt in attempts:
            for c in characters:
                permutation = attempt + c
                new_attempts.append(permutation)
                yield permutation
        attempts = new_attempts


def print_at(text: str, x: int, y: int):
    """ Prints `text` at a specific coordinate in the terminal.
    """
    print(f'\033[{y};{x}H{text}')


if __name__ == '__main__':
    # Tuple of iterables containing all the characters to use. In this case,
    # just numeric digits.
    charsets = (string.digits,)

    clearscreen()

    # Iterate through filename arguments provided
    for idx, filename in enumerate(sys.argv[1:]):
        print(f'{"Loading hash from file:":<25} {color(filename)}')

        # Read hash from file
        with open(filename, 'r') as f:
            target_hash = f.read().strip()

        print(f'{"Attempting to crack:":<25} {color(target_hash)}')

        # Iterate through permutations of `charsets`
        for permutation in permutator(''.join(charsets)):
            # Check permutation against hash
            success = sha1.verify(permutation, target_hash)

            # Report on current status
            status = color('CRACKED', 32) if success \
                else color('FAILED', 31)
            print_at(
                color(f'{permutation:<25}', 33) + f' {status}',
                0, 3 * (idx + 1) + (idx * 2)
            )

            if success:
                break

        print(f'Target hash source is: {permutation!r}.\n')
