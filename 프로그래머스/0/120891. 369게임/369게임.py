def solution(order):
    answer = 0
    numList = list(map(int, str(order)))
    for i in numList:
        if i in [3, 6, 9]:
            answer += 1
    return answer