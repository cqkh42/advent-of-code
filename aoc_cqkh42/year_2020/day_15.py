def part_a(data):
    nus = [int(num) for num in data.split(',')]
    nums = {num: index for index, num in enumerate(nus[:-1], 1)}
    last_num = nus[-1]
    for turn in range(len(nus)+1, 2021):
        v = nums.get(last_num, turn-1)
        nums[last_num] = turn - 1
        last_num = turn - 1 - v
    return last_num


def part_b(data, **_):
    nus = [int(num) for num in data.split(',')]
    nums = {num: index for index, num in enumerate(nus[:-1], 1)}
    last_num = nus[-1]
    for turn in range(len(nus)+1, 30000001):
        v = nums.get(last_num, turn-1)
        nums[last_num] = turn - 1
        last_num = turn - 1 - v
    return last_num
