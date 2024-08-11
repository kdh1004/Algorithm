def solution(str1, str2):
    for i in range(0,len(str1)):
        if str1[i:len(str2)+i] == str2:
            return 1
    return 2