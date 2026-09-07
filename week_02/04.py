def multiplyOrPlus():
    numStr = input("여러개의 숫자로 이루어진 문자열을 입력해주세요: ")
    result = int(numStr[0])
    for i in range(1, len(numStr)):
        n = int(numStr[i])
        ## 연산해야 할 두개의 숫자중 1개라도 0 또는 1 이면 (1보다 작거나 같으면)
        ## 그렇지 않으면 곱하고.
        if n <= 1 or result <= 1:
            result += n
        else:
            result *= n
    print(result)

if __name__ == "__main__":
    multiplyOrPlus()
