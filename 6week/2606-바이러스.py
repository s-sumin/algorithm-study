import sys
from collections import deque

# 입력: 정점(N)과 간선(M)의 개수를 읽음
N = int(sys.stdin.readline())  # 정점의 개수
M = int(sys.stdin.readline())  # 간선의 개수

# 그래프를 인접 리스트로 표현하기 위해 초기화
net = [[] for _ in range(N + 1)]  # 1번부터 N번까지의 정점

# 간선 정보 입력받아 그래프 구성
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)  # 정점 a에서 b로 가는 간선 추가
    net[b].append(a)  # 방향이 없는 그래프이므로 b에서 a로 가는 간선 추가

# BFS 함수 정의
def bfs():
    q = deque()  # 큐 생성
    count = 0  # 감염된 컴퓨터 수
    q.append(1)  # 1번 컴퓨터를 시작점으로 설정
    visited[1] = True  # 1번 컴퓨터를 방문 처리

    while q:  # 큐가 빌 때까지 반복
        cur = q.popleft()  # 큐에서 현재 정점(cur)을 꺼냄
        # 현재 정점과 연결된 모든 정점을 탐색
        for val in net[cur]:  
            if not visited[val]:  # 연결된 정점 중 아직 방문하지 않은 정점이 있다면
                q.append(val)  # 큐에 추가
                visited[val] = True  # 방문 처리
                count += 1  # 감염된 컴퓨터 수 증가

    print(count)  # 모든 감염이 끝난 후 결과 출력

# 방문 여부를 저장하는 배열 초기화
visited = [False for _ in range(N + 1)]  # 모든 정점을 방문하지 않은 상태로 초기화

# BFS 실행
bfs()
