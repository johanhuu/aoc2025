def manhattan_distance(
    pos1: list[int] | tuple[int, int], pos2: list[int] | tuple[int, int]
) -> int:
    assert len(pos1) == 2 and len(pos2) == 2, "Arguments must be of len == 2"
    return sum(abs(a - b) for a, b in zip(pos1, pos2))


def get_adjacent(r: int, c: int, r_lim: int, c_lim: int) -> tuple[tuple[int, int], ...]:
    """Returns positions NESW filtered on within bounds"""
    return tuple(
        (row, col)
        for (row, col) in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1))
        if row in range(r_lim) and col in range(c_lim)
    )


def get_adjacent_8(r: int, c: int, r_lim: int, c_lim: int) -> tuple[tuple[int, int], ...]:
    adjacent_8 = [
        *get_adjacent(r, c, r_lim, c_lim),
        *get_diagonal_ne(r, c, r_lim, c_lim, 1),
        *get_diagonal_se(r, c, r_lim, c_lim, 1),
        *get_diagonal_sw(r, c, r_lim, c_lim, 1),
        *get_diagonal_nw(r, c, r_lim, c_lim, 1),
    ]
    return tuple(adjacent_8)

def get_diagonal_ne(
    r: int, c: int, r_lim: int, c_lim: int, item_lim: int = -1
) -> tuple[tuple[int, int], ...]:
    positions: list[tuple[int, int]] = []
    cr, cc = r - 1, c + 1
    while cr >= 0 and cc < c_lim:
        positions.append((cr, cc))
        cr -= 1
        cc += 1
        if len(positions) == item_lim:
            break
    return tuple(positions)


def get_diagonal_se(
    r: int, c: int, r_lim: int, c_lim: int, item_lim: int = -1
) -> tuple[tuple[int, int], ...]:
    positions: list[tuple[int, int]] = []
    cr, cc = r + 1, c + 1
    while cr < r_lim and cc < c_lim:
        positions.append((cr, cc))
        cr += 1
        cc += 1
        if len(positions) == item_lim:
            break
    return tuple(positions)


def get_diagonal_sw(
    r: int, c: int, r_lim: int, c_lim: int, item_lim: int = -1
) -> tuple[tuple[int, int], ...]:
    positions: list[tuple[int, int]] = []
    cr, cc = r + 1, c - 1
    while cr < r_lim and cc >= 0:
        positions.append((cr, cc))
        cr += 1
        cc -= 1
        if len(positions) == item_lim:
            break
    return tuple(positions)


def get_diagonal_nw(
    r: int, c: int, r_lim: int, c_lim: int, item_lim: int = -1
) -> tuple[tuple[int, int], ...]:
    positions: list[tuple[int, int]] = []
    cr, cc = r - 1, c - 1
    while cr >= 0 and cc >= 0:
        positions.append((cr, cc))
        cr -= 1
        cc -= 1
        if len(positions) == item_lim:
            break
    return tuple(positions)
