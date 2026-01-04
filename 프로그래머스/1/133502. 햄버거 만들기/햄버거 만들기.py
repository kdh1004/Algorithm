def solution(ingredient):
    answer = 0
    sangsu = []
    
    for i in ingredient:
        sangsu.append(i)
        
        if sangsu[-4:] == [1,2,3,1]:
            
            del sangsu[-4:]
            answer += 1
            
    return answer