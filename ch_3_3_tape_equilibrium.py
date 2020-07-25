# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    subsum = []
    for i in range(len(A)):
        if i == 0:
            subsum.append(A[i])
        else:
            subsum.append(subsum[i-1]+A[i])

    diff = []
    totalsum = subsum[-1]
    for i in range(len(A)-1):
        left = subsum[i]
        right = totalsum - left
        _diff = abs(left-right)
        diff.append(_diff)
    return min(diff)

assert solution([3,1,2,4,3]) == 1
assert solution([1,2]) == 1
assert solution([1,2,3]) == 0
