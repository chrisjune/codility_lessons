# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N == 0:
        return 0

    N = bin(N)[2:]

    global_max = 0
    local_count = 0

    # cut off first element
    for idx, ele in enumerate(N[1:]):
        if ele == '1':
            global_max = max(global_max, local_count)
            local_count = 0

        elif ele == '0':
            local_count += 1
    return global_max


assert solution(32) == 0
assert solution(1041) == 5

