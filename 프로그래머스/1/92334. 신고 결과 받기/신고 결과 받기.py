def solution(id_list, report, k):
    answer = []
    answer = [0] * len(id_list)
    reported = {}
    for id in id_list:
        reported[id]=0
    
    for r in set(report):
        id1, id2 = r.split()
        reported[id2] += 1
        
    for r in set(report):
        id1, id2 = r.split()
        if reported[id2] >= k:
            answer[id_list.index(id1)]+=1
    
    return answer