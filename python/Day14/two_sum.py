

def two_sum(nums, target):
    seen = {}

    for i, x in enumerate(nums):
        needed = target -x
        # print(seen)
        if needed in seen:
            return seen[needed],i
        seen[x] = i
        # print(seen)
    return None  # when no pair found


print(two_sum([2, 7, 11, 15], 26))

