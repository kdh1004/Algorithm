def solution(s):
    answer = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]