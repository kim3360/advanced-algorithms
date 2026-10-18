def main():
    h = int(input())
    count = 0
    checkNum = 3
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if str(checkNum) in str(i) + str(j) + str(k):
                    count += 1
    print(count)
    return count

if __name__ == "__main__":
    main()
