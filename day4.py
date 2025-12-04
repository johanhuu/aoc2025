from helper import (
    get_adjacent_8,
)


def parse_input() -> list[str]:
    with open("files/input4.txt") as f:
        # with open("files/example4.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def part1(data) -> int:
    answer = 0
    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "@":
                adjacent8 = get_adjacent_8(r, c, rows, cols)
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
        pos_to_remove: list[tuple[int, int]] = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    adjacent8 = get_adjacent_8(r, c, rows, cols)
                    paper_nearby = sum(1 for cr, cc in adjacent8 if grid[cr][cc] == "@")
                    if paper_nearby < 4:
                        pos_to_remove.append((c, r))

        for dc, dr in pos_to_remove:
            grid[dr][dc] = "."
            answer += 1

        if not pos_to_remove:
            break

    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
