cnt = int(input())

for i in range(1,cnt+1):
    print("*"*i+str(' ')*(2*cnt-2*i)+str('*')*i)

for j in range(cnt-1,0,-1):
    print('*'*j+str(' ')*(2*(cnt-j))+str('*')*j)