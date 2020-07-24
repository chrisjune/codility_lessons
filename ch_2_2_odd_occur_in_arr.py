# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    newA = sorted(A)
    for i in range(0, len(newA), 2):
        if i == len(newA)-1:
            return newA[i]
        if newA[i] != newA[i+1]:
            return newA[i]

assert solution([1]) == 1
assert solution([2, 1, 2]) == 1
assert solution([1, 1, 1, 1, 3]) == 3
assert solution([3, 1, 1, 1, 1]) == 3
assert solution([1, 2, 3, 3, 2, 1, 4]) == 4
assert solution([9,3,9,3,9,7,9]) == 7

arr = []
for i in range(1,5000000+1):
    arr.append(i)
newarr = arr + arr[::-1] + [99999999999]

assert solution(newarr) == 99999999999

