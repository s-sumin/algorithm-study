n = int(input())
 
li = []
for i in str(n):
    li.append(int(i))
# li = list(map(int,str(n)))
    
li.sort(reverse=True) # 내림차순
 
for i in li:
    print(i,end='')