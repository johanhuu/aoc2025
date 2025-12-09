from collections import defaultdict


def parse_input():
    with open("files/input9.txt") as f:
    #with open("files/example9.txt") as f:
        return [
            tuple(reversed(tuple(map(int, line.rstrip().split(",")))))
            for line in f.readlines()
        ]


def part1(data) -> int:
    answer = 0
    tiles = [tile for tile in data]

    for t1 in tiles:
        for t2 in tiles:
            r1, c1 = t1
            r2, c2 = t2

            area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
            answer = max(area, answer)
    return answer


def build_lines(tile1, tile2, row_lines, col_lines):
    r1, c1 = tile1
    r2, c2 = tile2

    if r1 == r2:
        row_lines[r1].append((min(c1, c2), max(c1, c2)))
    elif c1 == c2:
        col_lines[c1].append((min(r1, r2), max(r1, r2)))
    else:
        print("CANNOT HAPPEN")


def is_within_bounds(tile, row_lines, col_lines):
    r, c = tile

    left_ok, right_ok, above_ok, below_ok = False,False,False,False

    left_ok = any(True for line in row_lines[r] if line[0] <= r) | any(
        True for col, lines in col_lines.items() for line in lines if col <= c and line[0] <= r <= line[1]
    )
    right_ok = any(True for line in row_lines[r] if line[1] >= r) | any(
        True for col, lines in col_lines.items() for line in lines if col >= c and line[0] <= r <= line[1]
    )
    above_ok = any(True for row, lines in row_lines.items() for line in lines if row <= r and line[0] <= c <= line[1]) | any(
        True for line in col_lines[c] if line[0] <= c
    )
    below_ok = any(True for row, lines in row_lines.items() for line in lines if row >= r and line[0] <= c <= line[1]) | any(
        True for line in col_lines[c] if line[1] >= c
    )


    return all([left_ok, right_ok, above_ok, below_ok])




def part2(data) -> int:
    answer = 0
    tiles = [tile for tile in data]

    # print(tiles)
    row_lines: dict[int, list[tuple[int, int]]] = defaultdict(list)
    col_lines: dict[int, list[tuple[int, int]]] = defaultdict(list)

    

    for i, tile in enumerate(tiles[:-1]):
        next_tile = tiles[i + 1]
        build_lines(tile, next_tile, row_lines, col_lines)
    build_lines(tiles[-1], tiles[0], row_lines, col_lines)

    print("num tiles: ", len(tiles))
    print("row lines : ", len(row_lines))
    print("col lines : ", len(col_lines))
    # idea check if virtual/opposite corners are in bounds

    # print(tiles)
    # for k, v in row_lines.items():
    #     print(k, v)
    # print("cols")
    # for k, v in col_lines.items():
    #     print(k, v)

    for t in tiles:
        if not (is_within_bounds(t, row_lines, col_lines)):
            print(t)
            is_within_bounds(t, row_lines, col_lines)
    
    # print(is_within_bounds((7,2), row_lines, col_lines))
    # print(is_within_bounds((3,6), row_lines, col_lines))

    print("num tiles: ", len(tiles))
    print("row lines : ", len(row_lines))
    print("col lines : ", len(col_lines))

    for i, t1 in enumerate(tiles):
        for t2 in tiles:
            r1, c1 = t1
            r2, c2 = t2

            v1 = (r1, c2)
            v2 = (r2, c1)


            if is_within_bounds(v1, row_lines, col_lines) and is_within_bounds(v2, row_lines, col_lines):
                area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
                
                #answer = max(area, answer)
                if area >= answer:
                    mid_point = (max(r1, r2) - min(r1,r2), max(c2, c1) - min(c1,c2))
                    if not is_within_bounds(mid_point, row_lines, col_lines):
                        continue
                    print(area)
                    answer = area
    
    print("row lines : ", len(row_lines))
    print("col lines : ", len(col_lines))
                  # 4748826374
    return answer # 4745405294 too high


def main() -> None:
    data = parse_input()
    print(f"Part 1 answer: {part1(data)}")
    print(f"Part 2 answer: {part2(data)}")


if __name__ == "__main__":
    main()
