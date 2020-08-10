def solution(A):
    maxlength = max(max(A), 0)
    dp = [False] * maxlength
    for ele in A:
        if ele > 0:
            dp[ele - 1] = True

    for idx, ele in enumerate(dp):
        if not ele:
            return idx + 1
    return maxlength + 1


assert solution([1]) == 2
assert solution([0]) == 1
assert solution([-1]) == 1
assert solution([-10]) == 1
assert solution([2]) == 1
assert solution([-1, -3]) == 1
assert solution([1, 2, 3]) == 4
assert solution([1, 3, 6, 4, 1, 2]) == 5
