cnt = int(input())

for i in range(1,cnt+1):
    print(' '*(cnt-i)+str('*')*i)

for j in range(cnt-1,0,-1):
    print(' '*(cnt-j)+str('*')*j)