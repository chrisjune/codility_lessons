# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    maxvalue = max(A)
    if len(A) < maxvalue:
        return 0

    dp = [0] * maxvalue
    for ele in A:
        dp[ele - 1] += 1

    for ele in dp:
        if ele != 1:
            return 0
    return 1


assert solution([100]) == 0
assert solution([1]) == 1
assert solution([2, 3]) == 0
assert solution([10, 11]) == 0
assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0
assert solution([1, 2, 3, 4, 5, 1, 6]) == 0
