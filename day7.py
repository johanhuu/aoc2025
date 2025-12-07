def parse_input():
    with open("files/input7.txt") as f:
        # with open("files/example7.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def get_start(grid: list[str]):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                return (r, c)
    return (-1, -1)


def part1(data) -> int:
    answer = 0
    rows = len(data)
    cols = len(data[0])

    sr, sc = get_start(data)
    beams: set[tuple[int, int]] = {(sr, sc)}

    while True:
        updated_beams: set[tuple[int, int]] = set()
        while beams:
            r, c = beams.pop()

            r += 1
            if r >= rows:
                continue

            if data[r][c] == "^":
                answer += 1
                if c - 1 >= 0:
                    left = (r, c - 1)
                    updated_beams.add(left)
                if c + 1 < cols:
                    right = (r, c + 1)
                    updated_beams.add(right)
            else:
                updated_beams.add((r, c))

        beams = updated_beams
        if not beams:
            break
    return answer


def part2(data) -> int:
    rows = len(data)
    cols = len(data[0])

    # kek lots of dead space in here but whatever
    tabu = [[0] * cols for _ in range(rows)]
    sr, sc = get_start(data)
    tabu[sr][sc] = 1

    for r in range(1, rows):
        for c in range(cols):
            above = tabu[r - 1][c]
            if data[r][c] == ".":
                tabu[r][c] += above
            elif data[r][c] == "^":
                tabu[r][c - 1] += above
                tabu[r][c + 1] += above

    return sum(tabu[-1])


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
