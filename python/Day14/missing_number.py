def find_missing(nums, n):
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

nums = list(range(1, 101))
nums.remove(49)

print(find_missing(nums, 100))
