def solution(start: int, end: int, jump_power: int) -> int:
    distance = end - start
    result = distance // jump_power
    if distance % jump_power != 0:
        result += 1
    return result

assert solution(10, 85, 30) == 3