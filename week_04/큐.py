

start = 1
def recursiveFunc_withFinish(i):
    print(f"{i}번째 함수가 호출되었습니다.")
    if i == 5:
        return

    print(f"{i}번째 함수가 종료되었습니다.")
    recursiveFunc_withFinish(i + 1)
    print(f"{i}번째 함수가 종료되었습니다.")

if __name__ == "__main__":
    recursiveFunc_withFinish(start)
