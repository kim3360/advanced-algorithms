h = int(input("시간을 입력하세요: "))

checkNum = 3

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if checkNum in str(i) + str(j) + str(k):
                count += 1
print(count)
