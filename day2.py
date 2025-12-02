
def parse_input() -> list[range]:
    data = []
    #with open("files/example2.txt") as f:
    with open("files/input2.txt") as f:
        for line in f.readlines():
            intervals = line.rstrip().split(",")
            for interval in intervals:
                begin, end = interval.split("-")
                data.append(range(int(begin), int(end) + 1))
    return data

def part1(data: list[range]) -> int:
    counter = 0
    for interval in data:
        for i in interval:
            s = str(i)
            size = len(s)
            if s[:size//2] == s[size//2:]:
                counter += i

    return counter


def part2(data: list[range]) -> int:
    counter = 0
    for interval in data:
        for i in interval:
            s = str(i)
            size = len(s)

            window_size = 1
            while window_size <= size // 2:
                window = s[0:window_size]
                max_repeat = size // window_size
                if window * max_repeat == s:
                    counter += i
                    break
                window_size += 1

    return counter


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
