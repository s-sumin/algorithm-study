cnt = int(input())
num_list = list(map(int,input().split()))

min = num_list[0]
max = num_list[0]

for i in range(cnt):
    if max<num_list[i]:
        max = num_list[i]
    
    elif min>num_list[i]:
        min = num_list[i]

print(min,max)