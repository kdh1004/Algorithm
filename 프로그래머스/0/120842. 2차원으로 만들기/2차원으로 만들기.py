def solution(num_list, n):
    a = []
    for i in range(0, len(num_list), n):
        a += [num_list[i:i+n]]
    return a