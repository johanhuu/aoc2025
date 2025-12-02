def parse_input() -> list[range]:
    # with open("files/example2.txt") as f:
    with open("files/input2.txt") as f:
        return [
            range(begin, end + 1)
            for line in f
            for interval in line.rstrip().split(",")
            for begin, end in [map(int, interval.split("-"))]
        ]


def part1(data: list[range]) -> int:
    return sum(
        [
            i
            for interval in data
            for i in interval
            if (s := str(i)) and s[: len(s) // 2] == s[len(s) // 2 :]
        ]
    )


def part2(data: list[range]) -> int:
    counter = 0
    for interval in data:
        for i in interval:
            s = str(i)
            size = len(s)

            for window_size in range(1, size // 2 + 1):
                window = s[0:window_size]
                max_repeat = size // window_size
                if window * max_repeat == s:
                    counter += i
                    break

    return counter


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
