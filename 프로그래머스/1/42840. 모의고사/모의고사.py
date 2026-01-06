def solution(answers):
    answer = [0,0,0]
    result = []
    
    q1 = [1,2,3,4,5]
    q2 = [2,1,2,3,2,4,2,5]
    q3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        ans = answers[i]
        if(q1[i%len(q1)] == ans):
            answer[0] += 1
        if(q2[i%len(q2)] == ans):
            answer[1] += 1
        if(q3[i%len(q3)] == ans):
            answer[2] += 1
            
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
        
    return sorted(result)