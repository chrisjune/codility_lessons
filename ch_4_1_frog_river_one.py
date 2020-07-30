# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    check = [False] * X
    cnt = 0
    for i in range(len(A)):
        if check[A[i] - 1] == False:
            check[A[i] - 1] = True
            cnt += 1
        if cnt == X:
            return i
    return -1


assert solution(2, [1, 2]) == 1
assert solution(3, [1, 2, 3]) == 2
assert solution(3, [1, 3, 2]) == 2
assert solution(5, [1,1,1,1,1,1,1,1]) == -1
assert solution(5, [1,3,1,4,2,3,5,4]) == 6
