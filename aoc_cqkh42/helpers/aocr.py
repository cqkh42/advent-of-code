"""
Parsing functions to identify characters from visual outputs.
"""
from typing import Any, Iterable

import more_itertools

from aoc_cqkh42.helpers.aocr_mappings import mappings

__all__ = ['letter', 'word']
#todo stop all auto suggests

def _format_row(row: Iterable[int], true=1) -> str:
    row = ''.join('#' if char == true else ' ' for char in row)
    return row


def letter(text: Iterable[Iterable[int]], true=1) -> str:
    """
    Parse a visual letter into a character. 6 Rows should be given as
    a 5 item list with a 1 to indicate a filled cell.
    Parameters
    ----------
    text: List of rows.
    Returns
    -------
    solution: str
    """
    rows = [_format_row(row, true) for row in text]
    text = '\n'.join(rows)
    solution = mappings[text]
    return solution


def word(characters: Iterable[Any], true=1) -> str:
    #todo make this take 2D arrays
    """
    Parse a visual word into a character.
    Parameters
    ----------
    characters: Iterable of the image, from left to right, top to
        bottom with 1 indicating a filled cell.
    Returns
    -------
    str
    """
    characters = [item for item in characters if item != '\n']
    rows = more_itertools.chunked(characters, len(characters)//6)
    blocks = (more_itertools.chunked(row, 5) for row in rows)
    answer = (letter(char, true) for char in zip(*blocks))
    return ''.join(answer)
