def parse_input() -> list[list[int]]:
    #with open("files/example3.txt") as f:
    with open("files/input3.txt") as f:
        return [list(map(int,list(line.rstrip()))) for line in f.readlines()]


def part1(data: list[list[int]]) -> int:
    answer = 0
    for battery in data:
        largest_idx, value = max(enumerate(battery[:-1]), key=lambda x: x[1])
        second_slice = battery[largest_idx + 1:]
        value2 = max(second_slice)
        answer += int(str(value) + str(value2))

    return answer


def part2(data: list[list[int]]) -> int:
    answer = 0
    for battery in data:
        first_idx, value = max(enumerate(battery[:-11]), key=lambda x: x[1])
        next_idx = first_idx + 1
        items = []

        for n in range(10, -1, -1):
            next_slice = battery[next_idx:-n] if n > 0 else battery[next_idx:]
            next_max_idx = battery.index(max(next_slice), next_idx)
            items.append(str(battery[next_max_idx]))
            next_idx = next_max_idx + 1
    
        answer += int(str(value) + "".join(items))

    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
