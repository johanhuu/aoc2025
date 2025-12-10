from functools import cache
from typing import Deque

def parse_input():
    lights = []
    buttons = []
    joltage = []
    #with open("files/input10.txt") as f:
    with open("files/example10.txt") as f:
        for line in f.readlines():
            line = line.rstrip()
            res = line.split(" ")
            lights.append(res[0].lstrip("[").rstrip("]"))
            tmp = []
            for button in res[1:-1]:
                button = button.lstrip("(").rstrip(")")
                tmp.append(tuple(map(int, button.split(","))))
            buttons.append(tuple(tmp))
            joltage.append(tuple(map(int, res[-1].lstrip("{").rstrip("}").split(","))))

    return lights, buttons, joltage


def part1(data) -> int:
    answer = 0
    lights, buttons, _  = data

    for i, light in enumerate(lights):
        current = [False] * len(light)
        target = [s == "#" for s in light]

        queue = Deque()
        queue.append((current, 0))

        while queue:
            c, steps = queue.popleft()
            if c == target:
                answer += steps
                break

            for button in buttons[i]:
                local_current = [item for item in c]
                for index in button:
                    local_current[index] = not local_current[index]
                queue.append((local_current, steps + 1))

    return answer

@cache
def solve(buttons, current, target, steps):
    ways = 100_000_000

    if current == target:
        return steps
    
    for button in buttons:
        local_current = list(current)
        for index in button:
            local_current[index] += 1
        if any(local_current[i] > target[i] for i in range(len(current))):
            continue
        res = solve(buttons, tuple(local_current), target, steps + 1)
        ways = min(ways, res)

    return ways

def part2(data) -> int:
    answer = 0
    _, buttons, joltage  = data

    for i, button_options in enumerate(buttons):
        print(i)
        target = joltage[i]
        current = (0,) * len(target)

        res = solve(tuple(sorted(button_options, key=len)), current, target, 0)
        answer += res

    return answer


def main() -> None:
    data = parse_input()
    #print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
