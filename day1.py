

def parse_input():
    with open("input1.txt") as f:
    #with open("example1.txt") as f:
        return [line.rstrip() for line in f.readlines()]

def part1(data):
    print(data)
    val = 50

    counter = 0
    for rotation in data:
        direction = rotation[0]
        increment = int(rotation[1:])

        if direction == "L":
            val -= increment
        else:
            val += increment

        while val > 99 or val < 0:
            if val > 99:
                val -= 100
            elif val < 0:
                val += 100

        if val == 0:
            counter += 1

    return counter


def part2(data):
    val = 50

    counter = 0
    for rotation in data:
        direction = rotation[0]
        increment = int(rotation[1:])

        for i in range(1, increment + 1):

            if direction == "L":
                val -= 1
            else:
                val += 1

            

            if val > 99:
                val -= 100
            elif val < 0:
                val += 100

            if val == 0:
                counter += 1
        

    return counter



def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()