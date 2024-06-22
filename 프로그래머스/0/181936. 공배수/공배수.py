def solution(number, n, m):
    if (number % n == 0 and number % m == 0):
        result = 1
    else:
        result = 0
    return result