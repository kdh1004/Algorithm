def solution(a, b, c):
    if a == b == c:
        return int(a+b+c) * int(a*a + b*b + c*c)*int(a*a*a + b*b*b + c*c*c)
    elif (a==b) or (b==c) or (a==c):
        return int(a+b+c)*int(a*a + b*b + c*c)
    else:
        return int(a+b+c)
    