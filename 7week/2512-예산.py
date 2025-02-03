import sys
input = sys.stdin.readline

N = int(input())  # 지방 수
budget = list(map(int, input().split()))  # 예산 요청 리스트
M = int(input())  # 총 예산

start, end = 0, max(budget)  # 이진 탐색 범위 설정

# 예산 요청의 총합이 총 예산 M 이하라면, 최대 요청 금액이 최적해
if sum(budget) <= M:
    print(max(budget))
else:
    while start <= end:
        mid = (start + end) // 2  # 중간값(상한액)

        # 상한액 기준으로 배정된 총 예산 계산
        total_budget = sum(min(mid, i) for i in budget)

        if total_budget > M:  # 총 예산 초과 시 상한액 줄이기
            end = mid - 1
        else:  # 총 예산 이하일 때, 더 높은 상한액을 탐색
            start = mid + 1

    print(end)  # 최적의 상한액 출력
