from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    
    count = 0
    max_count = len(q1+q2) * 2
    
    if (s1+s2) % 2 == 1:
        return -1
    
    if s1 == s2:
        return 0
    
    while True:
        if s1 > s2:
            i = q1.popleft()
            q2.append(i)
            
            s1 -= i
            s2 += i
            count += 1
        elif s2 > s1:
            i = q2.popleft()
            q1.append(i)
            
            s2 -= i
            s1 += i
            count += 1 
        else:
            break
        if count == max_count:
            return -1
        
    return count