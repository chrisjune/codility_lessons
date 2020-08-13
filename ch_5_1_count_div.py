# def solution(A, B, K)
#
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
#
# { i : A ≤ i ≤ B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
#
# Write an efficient algorithm for the following assumptions:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

from math import ceil


def solution(A, B, K):
    if A == B:
        return 1 if A % K == 0 else 0
    plus = 0
    start = ceil(A / K)
    end = B // K
    if A % K == 0:
        plus += 1
    if B % K == 0:
        plus += 1
    return end - start + 1


assert solution(6, 11, 2) == 3
assert solution(11, 345, 17) == 20
assert solution(0, 1, 11) == 1
assert solution(1, 1, 11) == 0
assert solution(0, 0, 11) == 1
assert solution(10, 10, 5) == 1
assert solution(0, 14, 2) == 8
assert solution(0, 4, 2) == 3
