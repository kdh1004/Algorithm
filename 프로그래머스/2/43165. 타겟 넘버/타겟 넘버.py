def bfs(numbers, num, i , answer,total,target):
    total += num

    if i == len(numbers)-1:
        if total == target:
            return answer + 1
                
    else:
        answer = bfs(numbers, numbers[i+1],i+1,answer,total,target)
        answer = bfs(numbers, -numbers[i+1],i+1, answer,total,target)
        
    return answer


def solution(numbers, target):
    answer = 0
    i = 0
    answer += bfs(numbers, numbers[i], 0, 0,0, target)
    answer += bfs(numbers, -numbers[i], 0, 0,0, target)
    
    return answer