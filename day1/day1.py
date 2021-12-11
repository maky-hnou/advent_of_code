def increases_nbr(lines):

    depths_tups = zip(lines, lines[1:])
    return len([1 for y, y1 in depths_tups if y1 > y])


if __name__ == '__main__':
    lines = [int(line) for line in open("day1.txt", "r").readlines()]
    window_sums = [x + y + z for x, y, z in zip(lines, lines[1:], lines[2:])]
    print(f'part1: {increases_nbr(lines)}, part2: {increases_nbr(window_sums)}')