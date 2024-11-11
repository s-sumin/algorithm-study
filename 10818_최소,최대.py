num = int(input()) #4
num2 = list(map(int, input().split()))
max = num2[0]
min = num2[0]
for i in num2[1:]: 
    if i>max:
        max = i
    elif i < min:
        min = i

print(min,max)

