import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가 (최대 10^6번까지 허용)
input = sys.stdin.readline  # 빠른 입력을 위한 sys.stdin.readline 사용

# 입력 받기
N = int(input())  # 영상의 크기 N (N은 항상 2^k 형태)
video = []  # 영상 정보를 저장할 리스트

# 영상 정보를 2차원 리스트로 저장
for _ in range(N):
    v = [int(x) for x in list(input().rstrip())]  # 문자열을 한 글자씩 정수로 변환하여 리스트로 저장
    video.append(v)

# 쿼드 트리 압축을 수행하는 재귀 함수
def quadtree(n, vlist):
    s = 0  # 현재 영역 내 모든 값의 합을 저장할 변수

    # 현재 영역의 모든 값의 합을 계산
    for l in vlist:
        s += sum(l)  # 리스트 내 값들을 모두 더함

    # 만약 모든 값이 '1'이라면 "1" 반환 (압축 가능)
    if s == n**2:
        return '1'
    
    # 만약 모든 값이 '0'이라면 "0" 반환 (압축 가능)
    if s == 0:
        return '0'
    
    # 위 조건을 만족하지 않으면 4등분하여 다시 검사
    half = n // 2  # 현재 영역을 4등분할 크기

    # 결과를 저장할 문자열 (괄호로 감싸기 위해 '(' 추가)
    temp = '('

    temp += quadtree(half, [l[:half] for l in vlist[:half]])

    temp += quadtree(half, [l[half:] for l in vlist[:half]])

    temp += quadtree(half, [l[:half] for l in vlist[half:]])

    temp += quadtree(half, [l[half:] for l in vlist[half:]])

    temp += ')'
    
    return temp  # 압축된 문자열 반환

# 결과 출력
print(quadtree(N, video))
