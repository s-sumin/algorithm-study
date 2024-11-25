cnt = int(input())
list = []
for i in range(cnt):
    num = int(input())
    if num == 0 :
        list.pop()
    else:
        list.append(num)


print(sum(list))