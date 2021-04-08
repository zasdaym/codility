def solution(num: int) -> int:
    """
    1. Convert the number to binary format.
    2. Remove extra 0b on the front from bin function.
    3. Strip all unnecessary 0s and 1s.
    4. Split string by 1, find max len.
    """
    max(len(bin(num)[:-2].strip("0").strip("1").split("1")))