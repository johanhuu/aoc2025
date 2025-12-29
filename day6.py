import math


def parse_input():
    num_row = []
    operators = []
    with open("files/input6.txt") as f:
        # with open("files/example6.txt") as f:
        for line in f.readlines():
            line = line.strip("\n")
            if "+" in line or "*" in line:
                operators = line
            else:
                num_row.append(line)
    return num_row, operators


def part1(data) -> int:
    nums, operators = data
    answer = 0

    numbers = [list(map(int, num.split())) for num in nums]
    ops = operators.split()
    problems = zip(*numbers)
    for i, problem in enumerate(problems):
        answer += sum(problem) if ops[i] == "+" else math.prod(problem)
    return answer


def part2(data) -> int:
    rows, operators = data
    answer = 0

    ops = operators.split()
    problem_count = 1
    nums: list[int] = []
    for i in range(len(operators) - 1, -2, -1):
        num = "".join(row[i] for row in rows)

        if num.isspace() or i == -1:
            operator = ops[-problem_count]
            answer += sum(nums) if operator == "+" else math.prod(nums)
            problem_count += 1
            nums.clear()
        else:
            nums.append(int(num))

    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
