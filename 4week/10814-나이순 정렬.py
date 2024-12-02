import sys
input = sys.stdin.readline
N = int(input())

# 2. member를 리스트로 입력받기
# N번 반복하여 회원 정보를 입력받음
# 각 줄은 공백으로 구분되므로, split()으로 나눔
# 각 회원 정보는 [나이(str), 이름(str)] 형태로 리스트에 저장
members = [list(map(str, input().split())) for _ in range(N)]

# 3. 정렬하기
# sort() 메서드를 사용하여 members 리스트를 정렬
# key=lambda x: int(x[0])로 정렬 기준을 첫 번째 값(나이)으로 설정
# x[0]은 문자열로 저장되므로 정수(int)로 변환하여 비교
# Python의 sort()는 안정 정렬이므로, 나이가 같으면 입력 순서가 유지됨
members.sort(key=lambda x: int(x[0]))

# 4. 원하는 형식으로 출력하기
# 정렬된 members 리스트에서 각 회원 정보를 출력
# *member를 사용하여 리스트 요소를 공백으로 구분하여 출력
for member in members:
    print(*member)

"""
num = int(input())
mem_list = []
for i in range(num):
    mem = input().split()
    mem[0] = int(mem[0])  # 첫 번째 값을 정수로 변환
    mem_list.append((mem, i))  # 데이터를 튜플로 저장: (데이터, 입력 순서)

# 정렬 구현
for i in range(len(mem_list)):
    for j in range(i + 1, len(mem_list)):
        if mem_list[i][0][0] > mem_list[j][0][0]:  # 숫자가 더 큰 경우
            mem_list[i], mem_list[j] = mem_list[j], mem_list[i]
        elif mem_list[i][0][0] == mem_list[j][0][0]:  # 숫자가 같은 경우
            if mem_list[i][1] > mem_list[j][1]:  # 입력 순서를 비교
                mem_list[i], mem_list[j] = mem_list[j], mem_list[i]

# 결과 출력
for item, _ in mem_list:
    print(item)
"""