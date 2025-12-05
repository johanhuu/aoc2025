def parse_input() -> tuple[list[range], list[int]]:
    ranges = []
    ids = []

    with open("files/input5.txt") as f:
        # with open("files/example5.txt") as f:
        for line in f.readlines():
            line = line.rstrip()
            if "-" in line:
                start, end = line.split("-")
                ranges.append(range(int(start), int(end) + 1))
            elif line.isnumeric():
                ids.append(int(line))
    return ranges, ids


def part1(data: tuple[list[range], list[int]]) -> int:
    answer = 0
    ranges, ids = data

    for id in ids:
        for r in ranges:
            if id in r:
                answer += 1
                break

    return answer


def part2(data: tuple[list[range], list[int]]) -> int:
    ranges, _ = data
    ranges.sort(key=lambda r: r[0])

    # gg ranges aren't mutable
    intervals = []
    for r in ranges:
        intervals.append([r[0], r[-1]])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last = merged_intervals[-1]

        if current[0] <= last[1]:
            last[1] = max(current[1], last[1])
        else:
            merged_intervals.append(current)

    return sum(end - begin + 1 for begin, end in merged_intervals)


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
