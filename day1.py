def parse_input() -> list[str]:
    # with open("files/example1.txt") as f:
    with open("files/input1.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def part1(data: list[str]) -> int:
    value = 50
    counter = 0

    for rotation in data:
        direction = rotation[0]
        increment = int(rotation[1:])

        if direction == "L":
            increment *= -1
        value = (value + increment) % 100

        if value == 0:
            counter += 1

    return counter


def part2(data: list[str]) -> int:
    value = 50
    counter = 0

    for rotation in data:
        direction = rotation[0]
        increment = int(rotation[1:])

        for _ in range(increment):
            dvalue = -1 if direction == "L" else 1
            value = (value + dvalue) % 100

            if value == 0:
                counter += 1

    return counter


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
