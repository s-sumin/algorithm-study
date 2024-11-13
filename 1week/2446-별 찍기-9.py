cnt = int(input())

for i in range(cnt,0,-1):
    print(str(' ')*(cnt-i)+str('*')*(2*i-1))

for j in range(2,cnt+1):
    print(str(' ')*(cnt-j)+str('*')*(2*j-1))