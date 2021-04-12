from typing import List
from sys import maxsize


def solution(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    min_diff = maxsize
    for num in nums[:-1]:
        total_sum -= num
        left_sum += num
        diff = abs(total_sum - left_sum)
        min_diff = min(min_diff, diff)
    return min_diff


assert solution([3, 1, 2, 4, 3]) == 1
assert solution([-1000, 1000]) == 2000
assert solution([1, 1]) == 0
