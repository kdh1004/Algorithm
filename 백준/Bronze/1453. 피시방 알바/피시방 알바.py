n = int(input())
num = list(map(int, input().split()))
seat = set(num)
print(len(num) - len(seat))