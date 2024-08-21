def solution(polynomial):
    answer = ''
    count1 = 0
    count2 = 0
    function = polynomial.split(' + ')
    for i in function:
        if 'x' in i:
            if len(i) == 1:
                count1 += 1
                continue
            a = i.replace('x','')
            count1 += int(a)
        else:
            count2 += int(i)
    if count1 == 1:
        count1 = "" 
    if count2==0:
        return str(count1) + "x"
    elif count1 == 0:
        return str(count2)
    else:
        return str(count1) + "x" + " + " + str(count2)