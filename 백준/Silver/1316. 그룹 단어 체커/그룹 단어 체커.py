num = int(input())
cnt = 0

for i in range(num):
    words = input() 
    bow = []
    if len(words) == 1:
        cnt += 1
    else: 
        for j in range(len(words)):
            if j == 0:
                bow.append(words[0])
            elif j > 0:
                if words[j] == words[j-1]:
                    bow.append(words[j])
                    if j == len(words)-1:
                        cnt += 1
                    
                elif words[j] != words[j-1]: 
                    if words[j] not in bow:
                        if j == len(words)-1:
                            cnt += 1
                        else:
                            bow.append(words[j])
                    elif words[j] in bow: 
                        break
                
print(cnt)