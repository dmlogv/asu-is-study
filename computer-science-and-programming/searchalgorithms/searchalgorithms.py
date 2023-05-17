from typing import Sequence


def linear(obj, seq: Sequence):
    """Returns an index the first occurence of obj in seq using linear search

    Suitable for unsorted sequences.
    Throws ValueError if obj is not found in seq.

    Examples:
    >>> linear('javascript', ['forth', 'c', 'python', 'haskell', 'dart'])
    Traceback (most recent call last):
    ...
    ValueError: javascript not in sequence
    >>> linear('haskell', ['forth', 'c', 'python', 'haskell', 'dart'])
    3
    """
    for i in range(len(seq)):
        if seq[i] == obj:
            return i
    else:
        raise ValueError(f'{obj} not in sequence')


def binary(obj, seq: Sequence):
    """Returns an index the random occurence of obj in seq using binary search

    obj and elements of seq must be an instance of comparable type.

    Suitable for the sorted sequences only.
    Throws ValueError if obj is not found in seq.

    Examples:
    >>> binary(-10, [-6, 0, 10, 15, 16, 17, 18, 20, 23, 34.5, 42, 43])
    Traceback (most recent call last):
    ...
    ValueError: -10 not in sequence
    >>> binary(42, [-6, 0, 10, 15, 16, 17, 18, 20, 23, 34.5, 42, 43])
    10
    >>> binary(-6, [-6, 0, 10, 15, 16, 17, 18, 20, 23, 34.5, 42, 43])
    0
    >>> binary(11, [-6, 0, 10, 15, 16, 17, 18, 20, 23, 34.5, 42, 43])
    Traceback (most recent call last):
    ...
    ValueError: 11 not in sequence
    >>> binary(42, [])
    Traceback (most recent call last):
    ...
    ValueError: 42 not in sequence
    >>> binary(42, [42])
    0
    >>> binary(42, [41, 42])
    1
    >>> binary(42, [41, 42, 43])
    1
    >>> binary(42, [0, 1, 42])
    2
    """
    start_pos = 0
    end_pos = len(seq) - 1

    while start_pos <= end_pos:
        mid_pos = (start_pos + end_pos) // 2

        if obj == seq[mid_pos]:
            return mid_pos
        elif obj < seq[mid_pos]:
            end_pos = mid_pos - 1
        else:
            start_pos = mid_pos + 1

    raise ValueError(f'{obj} not in sequence')


def jump(obj, seq: Sequence):
    pass


def fibonacci(obj, seq: Sequence):
    pass


def exponential(obj, seq: Sequence):
    pass


def interpolation(obj, seq: Sequence):
    pass
