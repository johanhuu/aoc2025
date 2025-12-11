from collections import defaultdict
from functools import cache
from typing import Deque


def parse_input() -> dict[str, list[str]]:
    data = defaultdict(list)
    # with open("files/example11.txt") as f:
    with open("files/input11.txt") as f:
        for line in f.readlines():
            node, links = line.rstrip().split(":")
            data[node].extend(links.split())
    return data


def bfs(data) -> int:
    queue: Deque[str] = Deque()
    queue.extend(data["you"])

    counter = 0
    while queue:
        node = queue.pop()
        if node == "out":
            counter += 1
        else:
            queue.extend(data[node])

    return counter


def part1(data) -> int:
    return bfs(data)


def part2(data) -> int:
    @cache
    def memo(node, dac, fft) -> int:
        if node == "out":
            return dac & fft
        elif node == "dac":
            dac = True
        elif node == "fft":
            fft = True
        return sum(memo(neighbor, dac, fft) for neighbor in data[node])

    return memo("svr", False, False)


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
