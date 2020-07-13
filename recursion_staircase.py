# get the number of ways you could get up a flight of stairs with n number of steps


def num_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return num_ways(n-1) + num_ways(n-2) + num_ways((n-3))

def num_ways_memoized(n):
    nums = [1, 1, 2, 4]
    for x in range(4, n + 1):
        nums.append(nums[x - 1] + nums[x - 2] + nums[x - 3])
    return nums[n]


for i in range(7):
    combos = num_ways(i)
    formatted_string = "for {} stairs there are {} combinations.".format(i, combos)
    print(formatted_string)

print(num_ways_memoized(6))