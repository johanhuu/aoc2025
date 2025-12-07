def parse_input():
    #with open("files/input.txt") as f:
    with open("files/example.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def part1(data) -> int:
    answer = 0

    return answer


def part2(data) -> int:
    answer = 0

    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
