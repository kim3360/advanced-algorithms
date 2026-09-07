def adventureGuild():
    n = int(input("모험가의 수를 입력해주세요: "))
    data = list(map(int, input(f"모험가 {n}명의 공포도를 입력해주세요: ").split()))
    data.sort()

    result = 0
    count = 0

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0
    print(f"여행을 떠날 수 있는 최대 그룹 수 = {result}")

if __name__ == "__main__":
    adventureGuild()
