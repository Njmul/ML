
def deduplicate(nums):
    seen = set()
    out = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
print(deduplicate([1, 1, 2, 3, 1, 4]))
