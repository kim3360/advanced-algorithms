def main():
    data = input()
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in data:
        if x.isalpha():
            result.append(x)

        else:
            value += int(x)

    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))
    print(''.join(result))
    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)

if __name__ == "__main__":
    main()
