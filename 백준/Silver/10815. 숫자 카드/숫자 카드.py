# 입력 처리
N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

# 결과 리스트
result = []

# 각 M의 요소가 N_set에 있는지 확인
for num in M_list:
    if num in N_set:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(" ".join(map(str, result)))
