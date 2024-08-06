def solution(s):
    answer = ''
    list = []
    
    for i in s:
        if s.count(i)==1:
            list.append(i)
    list.sort()
    answer="".join(list)
    return answer