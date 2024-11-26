cnt = int(input())
list=[]
for i in range(cnt):
    num = int(input())
    list.append(num)

list.sort() #sort는 리스트를 제자리에서 정렬한다. 따라서 정렬 후 리스트를 직접 출력
print(list) #바로 print(list.sort()) 하면 안되는 이유는 list.sort()는 리스트를 정렬하지만, 반환값이 none이기 때문
#sorted_list = sorted(list)
#print(sorted_list)


