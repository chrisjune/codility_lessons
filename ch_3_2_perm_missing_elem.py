def solution(A):
    if not A:
        return 1
    
    A = sorted(A)
    result = len(A) + 1
    for i in range(len(A)):
        if A[i] != i+1:
            result = i+1
            break
    return result


assert solution([]) == 1
assert solution([1]) == 2
assert solution([1,2]) == 3
assert solution([1,3,4]) == 2
assert solution([5,4,3,2]) == 1

