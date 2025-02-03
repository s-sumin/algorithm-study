import sys

# 입력 받기
N = int(sys.stdin.readline())  
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 개수 저장할 변수 (-1, 0, 1 종이 개수)
count_minus1 = 0
count_0 = 0
count_1 = 0

# 분할 정복 함수
def cut(row, col, n):
    global count_minus1, count_0, count_1
    first_value = paper[row][col]  # 현재 영역의 첫 번째 값 저장

    # 현재 영역이 모두 같은 숫자인지 확인
    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[i][j] != first_value:  # 다른 숫자가 하나라도 있다면 9등분
                size = n // 3  # 새로운 크기 (n을 3등분)
                for a in range(3):
                    for b in range(3):
                        cut(row + a * size, col + b * size, size)  # 9개로 나누어 재귀 호출
                return  # 9등분 후에는 더 이상 진행하지 않음

    # 만약 영역이 하나의 숫자로만 이루어졌다면, 해당 숫자의 개수를 증가
    if first_value == -1:
        count_minus1 += 1
    elif first_value == 0:
        count_0 += 1
    else:
        count_1 += 1

# 전체 영역(0,0)에서 시작하여 N x N 검사
cut(0, 0, N)

# 결과 출력
print(count_minus1)
print(count_0)
print(count_1)
