def parse_input() -> list[list[int]]:
    #with open("files/example3.txt") as f:
    with open("files/input3.txt") as f:
        return [list(map(int,list(line.rstrip()))) for line in f.readlines()]


def part1(data: list[list[int]]) -> int:
    ans = 0
    for battery in data:
        largest = "0"
        largest_index = battery[:-1].index(max(battery[:-1]))
        
        if largest_index == len(battery) - 2:
            largest = str(battery[largest_index]) + str(battery[-1])
        else:
            second_slice = battery[largest_index + 1:]
            second_largest = battery[battery.index(max(second_slice), largest_index + 1)]
            largest = str(battery[largest_index]) + str(second_largest)
        
        ans += int(largest)
    

    return ans


def part2(data: list[list[int]]) -> int:
    ans = 0
    for battery in data:
        largest = "0"
        
        first_index = battery.index(max(battery[:-11]))
        
        if first_index == len(battery) - 12:
            rest = "".join(map(str, battery[first_index + 1:]))
            largest = str(battery[first_index]) + rest
        else:
            next_index = first_index + 1
            items = []
            for n in range(10, -1, -1):
                next_slice = battery[next_index:-n] if n > 0 else battery[next_index:]
                next_max = battery.index(max(next_slice), next_index)
                next_value = str(battery[next_max])
                items.append(next_value)

                next_index = next_max + 1
        
            largest = str(battery[first_index]) + "".join(items)
        ans += int(largest)

    return ans


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
