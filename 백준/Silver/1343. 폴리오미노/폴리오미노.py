N=str(input())
N=N.replace('XXXX','AAAA')
N=N.replace('XX','BB')

if 'X' in N:
    print(-1)
else:
    print(N)