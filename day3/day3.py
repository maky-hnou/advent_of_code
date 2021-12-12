import numpy as np


def day3(array):
    gamma = ''
    o2_array = array
    co2_array = array
    for i in range(array.shape[1]):
        most_common_bit = np.bincount(array[:, i]).argmax()
        gamma += str(most_common_bit)

        if o2_array.shape[0] > 1:
            occurrences = np.bincount(o2_array[:, i])
            most_common_bit_ = max(np.where(occurrences == max(occurrences))[0])
            o2_array = o2_array[o2_array[:, i] == most_common_bit_]

        if co2_array.shape[0] > 1:
            occurrences = np.bincount(co2_array[:, i])
            least_common_bit_ = min(np.where(occurrences == min(occurrences))[0])
            co2_array = co2_array[co2_array[:, i] == least_common_bit_]

    co2_rate = np.apply_along_axis(lambda row: row.astype('|S1').tobytes().decode('utf-8'),
                                   axis=1,
                                   arr=co2_array)
    o2_rate = np.apply_along_axis(lambda row: row.astype('|S1').tobytes().decode('utf-8'),
                                  axis=1,
                                  arr=o2_array)
    co2_rate = int(co2_rate[0], 2)
    o2_rate = int(o2_rate[0], 2)

    power_rate = int(gamma, 2) * int(gamma.translate(str.maketrans('10', '01')), 2)
    life_rate = co2_rate * o2_rate

    print(f'part1: {power_rate}, part2: {life_rate}')


if __name__ == '__main__':
    lines = list(map(list, open('day3.txt').read().splitlines()))
    arr = np.array(lines, dtype=int)
    day3(arr)

