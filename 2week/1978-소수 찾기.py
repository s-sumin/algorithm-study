num = input()
M,N = map(int,input().split())
for i in range(M,N+1): #9
    if i ==1:
        continue
    for j in range(2,i): #2345678
        if i % j == 0: #9/2
            break
    else:
        print(len(i))
