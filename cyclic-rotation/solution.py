from typing import List

def solution(nums: List[int], rotate_count: int) -> List[int]:
    """
    1. Reverse the array.
    2. Reverse first k-items (modulo k with array length first) with in the array.
    3. Reverse last remaining items in the array.
    """
    if len(nums) <= 1:
        return nums

    rotate_count %= len(nums)
    if rotate_count == 0:
        return nums
    
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, rotate_count - 1)
    reverse(nums, rotate_count, len(nums)-1)
    return nums

def reverse(nums: List[int], start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1