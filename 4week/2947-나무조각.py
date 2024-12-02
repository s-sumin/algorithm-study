li = list(map(int, input().split()))  #31245
for i in range(5):
    for j in range(4):
        # 현재 요소(li[j])가 다음 요소(li[j+1])보다 크다면 자리 교환
        if li[j] > li[j + 1]: #3>1
            # 두 요소를 스왑 (교환)하는 과정
            # li[j] 값을 임시 변수 t에 저장
            t = li[j]   #t=3
            # li[j]에 li[j+1] 값을 대입
            li[j] = li[j + 1]   #1저장(맨앞에)
            # li[j+1]에 임시 변수 t 값을 대입 (교환 완료)
            li[j + 1] = t   #두번째로 3저장(t)
            
            #결합된 문자열을 출력.
            print(" ".join(map(str, li))) 