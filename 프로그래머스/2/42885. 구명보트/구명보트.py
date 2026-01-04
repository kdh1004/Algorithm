def solution(people, limit):
    answer = 0
    
    people.sort()
    
    lightNo = 0
    heavyNo = len(people)-1
    
    while(lightNo <= heavyNo):
        if people[heavyNo] + people[lightNo] <= limit:
            lightNo += 1
        heavyNo -= 1
        answer += 1
    return answer