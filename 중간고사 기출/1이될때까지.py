# 1이 될때까지 문제
#첫 째줄 n, k 입력
#둘째줄 n이 1이 될때까지 1빼기 혹은 k로 나누기 연산을 수행해야하는 최소 횟수 출력


def main():
   n, k = map(int, input().split()) # 입력
   result = 0
   while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
   while n > 1:
    n -= 1
    result += 1
   print(result)
   return result
if __name__ == "__main__":
    main()
