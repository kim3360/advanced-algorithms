from datetime import datetime

## 함수나 로직...
def programstart():
    print("Program started")

## 함수들 불러서, 실행

    def getChangeCnt():
        n = 1260
        count = 0

    array = [500, 100, 50, 10]
    for coin in array:
        count += n // coin
        n %= coin
    print(f"거슬러 주어야 할 동전의 최소 갯수 = {count}개")



########################################################
########################################################
## 필요한 함수들 정의

def getCurrentTimeStr():
    currentTimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "[" + currentTimeStr + "]"

if __name__ == "__main__":
    ## 현재 시간을 확인해서 시작 시간으로 저장
    start_time = datetime.now()
    ## 종료 시간 - 시작 시간을 실행 시간으로 확인
    print(getCurrentTimeStr(),"This is Main Start")
    print(getCurrentTimeStr(), "Total 000 elapsed..")
    ## 현재 시간을 확인해서 종료 시간으로 저장
    ## 종료 시간 - 시작 시간을 실행 시간으로 확인
    print("Program ended")
