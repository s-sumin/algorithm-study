num = int(input())

pivolist=[0,1]
for i in range(2,num+1):
    pivolist.append(pivolist[i-2]+pivolist[i-1])

print(pivolist[num])