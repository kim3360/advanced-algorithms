def getMinimumCalCnt():
    n, k = map(int, input("N과 K를 공백으로 띄어서 입력하라: ").split())
    result = 0
    while n >= k:
       # N이 K로 나누어 떨어지면, K로 나누고 (연산+1)
       # 이게 안되면, 될때까지 -1(연산+1) 반복

    #  while (n % k) != 0:
    #    n = n - 1
    #    result = result + 1

     target = (n // k) * k
     result = result + (n - target)
     n = target

     if n > k :
        break

    n = n // k
    result = result + 1

    # while n > 1 :
    #     n = n - 1
    #     result  = result + 1

    result = result + (n - 1)

    print(result)


if __name__ == "__main__":
    getMinimumCalCnt()
