def solution(lines):
    total_space = [0] * 202
    
    for line in lines:
        for i in range(line[0]+1,line[-1]+1):
            total_space[i+100] += 1
            
    answer =0
    
    print(total_space)
    for i in range(1,len(total_space)):
        if total_space[i] > 1 :
            answer +=1

    return answer