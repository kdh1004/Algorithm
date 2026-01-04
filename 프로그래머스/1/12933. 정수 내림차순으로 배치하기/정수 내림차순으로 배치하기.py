def solution(n):
    result = sorted(str(n), reverse=True)
    
    answer=''
    for i in range(len(str(n))):
        answer += result[i]
        
    return int(answer)