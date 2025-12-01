def solution(nums):
    hash = {}
    for i in nums:
        hash[i] = 1

    kinds = len(hash)
    limit = len(nums) // 2
    return min(kinds, limit)
