from typing import Deque
import z3  # type: ignore


def parse_input():
    lights = []
    buttons = []
    joltage = []
    with open("files/input10.txt") as f:
        # with open("files/example10.txt") as f:
        for line in f.readlines():
            segments = line.rstrip().split()
            lights.append(segments[0].lstrip("[").rstrip("]"))
            tmp = []
            for button in segments[1:-1]:
                button = button.lstrip("(").rstrip(")")
                tmp.append(tuple(map(int, button.split(","))))
            buttons.append(tuple(tmp))
            joltage.append(
                tuple(map(int, segments[-1].lstrip("{").rstrip("}").split(",")))
            )

    return lights, buttons, joltage


def part1(data) -> int:
    answer = 0
    lights, buttons, _ = data

    for i, light in enumerate(lights):
        current = [False] * len(light)
        target = [s == "#" for s in light]

        queue = Deque()  # type: ignore
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


# rip dp rip dijkstra is this really how it's meant to be solved???
def part2(data) -> int:
    answer = 0
    _, buttons, joltage = data

    for i, button_options in enumerate(buttons):
        target = joltage[i]
        num_cols = len(target)

        buttons = []
        for button in button_options:
            b = [0] * num_cols
            for index in button:
                b[index] += 1
            buttons.append(b)

        num_buttons = len(buttons)
        variables = [z3.Int(str(i)) for i in range(num_buttons)]  # type: ignore  # noqa: F405

        opt = z3.Optimize()  # type: ignore  # noqa: F405

        for var in variables:
            opt.add(var >= 0)

        for col in range(num_cols):
            opt.add(
                sum(variables[i] * buttons[i][col] for i in range(num_buttons))
                == target[col]
            )

        opt.minimize(sum(variables))
        if opt.check() != z3.sat:  # type: ignore  # noqa: F405
            print("Solution not found")
            exit(-1)

        m = opt.model()
        ans = sum(m[var].as_long() for var in variables)  # type: ignore  # noqa: F405
        answer += ans

    return answer


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
