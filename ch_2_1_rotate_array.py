# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if K == 0 or A == []:
        return A
    K = K % len(A)

    point = len(A) - K
    return A[point:] + A[:point]

assert solution([], 1) == []
assert solution([1], 1) == [1]
assert solution([1,2,3,4], 4) == [1,2,3,4]
assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([-4], 0) == [-4]
assert solution([1, 1, 2, 3, 5], 6) == [5, 1, 1, 2, 3]
