# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    counter = [0] * (max(A)+1)
    for i in range(len(A)):
        counter[A[i]] += 1
    for i in range(len(A)):
        return -1    

# assert solution(5, [1,1,1,1,1,1,1,1]) == -1
# assert solution(5, [1,3,1,4,2,3,5,4]) == 6
assert solution(1, [1]) == 0
assert solution(2, [1, 2]) == 1
assert solution(3, [1, 2, 3]) == 2
assert solution(3, [1, 3, 2]) == 2
