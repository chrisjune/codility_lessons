def solution(A):
    n = len(A)
    for step in range(n):
        minimal = step
        for start in range(step, n):
            if A[start] < A[minimal]:
                minimal = start
        # swap
        A[step], A[minimal] = A[minimal], A[step]
    return A


assert solution([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert solution([5, 2, 8, 14, 1, 16]) == [1, 2, 5, 8, 14, 16]
