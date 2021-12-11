import re


def calculate_position(lines):
    forward = 0
    depth = 0
    aim = 0
    for line in lines:
        steps = re.search(r'\d+', line).group(0)
        if 'forward' in line:
            forward += int(steps)
            depth += aim * int(steps)
        elif 'up' in line:
            aim -= int(steps)
        elif 'down' in line:
            aim += int(steps)

    return forward * aim, depth * forward


if __name__ == '__main__':
    lines = open("day2.txt", "r").readlines()
    part1, part2 = calculate_position(lines)
    print(f'part1: {part1}, part2: {part2}')
