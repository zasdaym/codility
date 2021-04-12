from typing import List

def solution(nums: List[int]) -> int:
    max_element = len(nums) + 1
    expected_sum = (max_element + 1) * max_element / 2
    result = expected_sum - sum(nums)
    return int(result)

assert solution([1, 2, 3, 5]) == 4