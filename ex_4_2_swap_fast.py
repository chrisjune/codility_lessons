def solution(A, B):
    sum_a = sum(A)
    sum_b = sum(B)
    diff = sum_a - sum_b
    if diff % 2 == 1:
        return False

    d = diff // 2
    # a = b - d
    counting_a = counting(A)
    for i in range(len(A)):
        b = B[i]
        if 0 <= b - d < len(A) and counting_a[b - d] > 0:
            return True
    return False


def counting(A):
    l = [0] * len(A)
    for i in range(len(A)):
        a = A[i]
        l[a] += 1
    return l


assert solution([1, 2, 2], [1, 3, 3])
assert not solution([0, 2, 3, 100], [2, 2, 3, 99])
