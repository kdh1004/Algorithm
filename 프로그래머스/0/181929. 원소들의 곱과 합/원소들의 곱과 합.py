def solution(num_list):
    sum = 0
    mul = 1
    answer = 0
    
    for i in range(len(num_list)):
        sum += num_list[i]
        mul *= num_list[i]
        
    if mul < sum**2 :
        answer = 1
    else:
        answer = 0
    return answer