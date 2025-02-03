import sys  # 표준 입력을 빠르게 받기 위해 sys 모듈 사용

# N 입력 받기 (종이의 크기)
N = int(sys.stdin.readline())

# N x N 크기의 정사각형 종이 정보 입력 받기
square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 흰색(0)과 파란색(1) 종이의 개수를 저장할 변수
white = 0
blue = 0

# 종이를 자르는 함수 정의
def cut(row, column, n):
    global white, blue 
    color = square[row][column]  # 현재 영역의 첫 번째 색깔 저장

    # 현재 영역이 모두 같은 색인지 확인
    for i in range(row, row + n):
        for j in range(column, column + n):
            if color != square[i][j]:  # 하나라도 다른 색이 있으면 나눈다
                cut(row, column, n // 2)  # 1사분면 (좌상단)
                cut(row, column + n // 2, n // 2)  # 2사분면 (우상단)
                cut(row + n // 2, column, n // 2)  # 3사분면 (좌하단)
                cut(row + n // 2, column + n // 2, n // 2)  # 4사분면 (우하단)
                return  # 더 이상 진행하지 않음

    # 모든 영역이 같은 색이라면, 해당 색깔의 종이 개수를 증가
    if color == 0:
        white += 1  # 흰색 종이 개수 증가
    else:
        blue += 1  # 파란색 종이 개수 증가

# (0,0)에서 시작하여 전체 종이를 검사
cut(0, 0, N)

# 결과 출력
print(white)  # 흰색 종이 개수 출력
print(blue)   # 파란색 종이 개수 출력
