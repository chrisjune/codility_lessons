# You are given N counters, initially set to 0, and you have two possible operations on them:
#
# A non-empty array A of M integers is given. This array represents consecutive operations:
#
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:
#
#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.
#
# Write a function:
#
# def solution(N, A)
#
# that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.
#
# Result array should be returned as an array of integers.
#
# For example, given:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].


def solution(N, A):
    global_max = 0
    local_max = 0
    output = [0] * N
    for ele in A:
        index = ele - 1
        if ele > N:
            local_max = global_max
            continue

        if output[index] < local_max:
            output[index] += (local_max + 1)
        else:
            output[index] += 1
        global_max = max(global_max, output[index])

    for i in range(len(output)):
        if output[i] < local_max:
            output[i] = local_max
    return output


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
assert solution(1, [2, 2, 2, 2]) == [0]
assert solution(2, [2]) == [0, 1]
print(solution(5, [6, 6, 6, 6, 6, 6]))
assert solution(5, [1, 2, 3, 1, 6, 6, 6, 6, 6]) == [2, 2, 2, 2, 2]
