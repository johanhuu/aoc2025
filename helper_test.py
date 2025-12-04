import pytest
from helper import (
    get_adjacent_8,
    get_diagonal_ne,
    get_diagonal_nw,
    get_diagonal_se,
    get_diagonal_sw,
    manhattan_distance,
    get_adjacent,
)


def test_manhattan_distance_lists():
    assert manhattan_distance([2, 1], [5, 5]) == 7


def test_manhattan_distance_tuples():
    assert manhattan_distance((5, 1), (3, 3)) == 4


def test_manhattan_distance_mixed():
    assert manhattan_distance([1, 1], (3, 3)) == 4


def test_invalid_input():
    with pytest.raises(AssertionError):
        manhattan_distance([1, 2, 3], (5, 5))


def test_get_adjacent_centered():
    res = get_adjacent(2, 2, 10, 10)
    assert res == ((1, 2), (2, 3), (3, 2), (2, 1))


def test_get_adjacent_left_upper():
    res = get_adjacent(0, 0, 10, 10)
    assert res == ((0, 1), (1, 0))


def test_get_adjacent_bottom_right():
    res = get_adjacent(9, 9, 10, 10)
    assert res == ((8, 9), (9, 8))


def test_get_diagonal_ne():
    res = get_diagonal_ne(7, 7, 10, 10)
    assert res == ((6, 8), (5, 9))
    assert get_diagonal_ne(7, 7, 10, 10, 1) == ((6, 8),)


def test_get_diagonal_se():
    res = get_diagonal_se(7, 7, 10, 10)
    assert res == ((8, 8), (9, 9))
    assert get_diagonal_se(7, 7, 10, 10, 1) == ((8, 8),)


def test_get_diagonal_sw():
    res = get_diagonal_sw(7, 7, 10, 10)
    assert res == ((8, 6), (9, 5))
    assert get_diagonal_sw(7, 7, 10, 10, 1) == ((8, 6),)


def test_get_diagonal_nw():
    res = get_diagonal_nw(7, 7, 10, 10)
    assert res == ((6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0))
    assert get_diagonal_nw(7, 7, 10, 10, 3) == ((6, 6), (5, 5), (4, 4))


def test_get_adjacent_8():
    res = get_adjacent_8(3, 3, 10, 10)
    assert res == ((2, 3), (3, 4), (4, 3), (3, 2), (2, 4), (4, 4), (4, 2), (2, 2))
    res = get_adjacent_8(1, 0, 10, 10)
    assert res == ((0, 0), (1, 1), (2, 0), (0, 1), (2, 1))