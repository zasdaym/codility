from typing import List

def solution(nums: List[int]) -> int:
    """
    1. Create a set to track iterated numbers.
    2. Iterate every number
        1. if number not exists in set, add the number to the set and the result.
        2. If number is exists in set, remove the number from set and the result.
    3. The result sum will be the single unique number.
    """
    result = 0
    unique_nums = set()
    
    for num in nums:
        if num in unique_nums:
            result -= num
            unique_nums.remove(num)
        else:
            result += num
            unique_nums.add(num)
    
    return result