def solution(numbers):
    
    numbers.sort()
    
    answer1 = numbers[0] * numbers[1]
    answer2 = numbers[len(numbers)-1] * numbers[len(numbers)-2]

    if answer1 > answer2:
        return answer1
    else:
        return answer2