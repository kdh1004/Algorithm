N = int(input())
D, P = 0, 0
game = [input() for _ in range(N)]

for i in game:
    if i == "D":
        D += 1
    else:
        P += 1

    if abs(D - P) >= 2:
        break

print("{}:{}".format(D, P))