from helper import get_adjacent, get_diagonal_ne, get_diagonal_nw, get_diagonal_se, get_diagonal_sw


def parse_input():
    with open("files/input4.txt") as f:
    #with open("files/example4.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def part1(data) -> int:
    answer = 0
    rows = len(data)
    cols = len(data[0])
    
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "@":
                adjacent8: list[tuple[int, int]] = []
                adjacent8.extend(get_adjacent(r, c, rows, cols))
                diag_ne = get_diagonal_ne(r, c, rows, cols)
                diag_se = get_diagonal_se(r, c, rows, cols)
                diag_sw = get_diagonal_sw(r, c, rows, cols)
                diag_nw = get_diagonal_nw(r, c, rows, cols)
                if len(diag_ne) > 0:
                    adjacent8.append(diag_ne[0])
                if len(diag_se) > 0:
                    adjacent8.append(diag_se[0])
                if len(diag_sw) > 0:
                    adjacent8.append(diag_sw[0])
                if len(diag_nw) > 0:
                    adjacent8.append(diag_nw[0])

                paper_nearby = sum(1 for cc, cr in adjacent8 if data[cc][cr] == "@")
                if paper_nearby < 4:
                    answer += 1

    return answer


def part2(data) -> int:
    answer = 0
    rows = len(data)
    cols = len(data[0])

    grid = [list(row) for row in data]
    
    while True:
        pos_to_remove: list[tuple[int,int]] = []
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "@":
                    adjacent8: list[tuple[int, int]] = []
                    adjacent8.extend(get_adjacent(r, c, rows, cols))
                    diag_ne = get_diagonal_ne(r, c, rows, cols)
                    diag_se = get_diagonal_se(r, c, rows, cols)
                    diag_sw = get_diagonal_sw(r, c, rows, cols)
                    diag_nw = get_diagonal_nw(r, c, rows, cols)
                    if len(diag_ne) > 0:
                        adjacent8.append(diag_ne[0])
                    if len(diag_se) > 0:
                        adjacent8.append(diag_se[0])
                    if len(diag_sw) > 0:
                        adjacent8.append(diag_sw[0])
                    if len(diag_nw) > 0:
                        adjacent8.append(diag_nw[0])

                    paper_nearby = sum(1 for cr, cc in adjacent8 if grid[cr][cc] == "@")
                    if paper_nearby < 4:
                        pos_to_remove.append((c, r))
        
        for dc, dr in pos_to_remove:
            grid[dr][dc] = "."
            answer += 1

        if not pos_to_remove:
            break
        else:
            pos_to_remove.clear()
    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
