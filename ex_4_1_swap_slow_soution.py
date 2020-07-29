def solution(A, B):
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(len(A)):
        for j in range(len(B)):
            a = A[i]
            b = B[j]
            sum_a = sum_a - a + b
            sum_b = sum_b - b + a
            if sum_a == sum_b:
                return True
            sum_a = sum_a - b + a
            sum_b = sum_b - a + b
    return False


assert solution([1, 2, 2], [1, 3, 3])
assert not solution([0, 2, 3, 100], [2, 2, 3, 99])
