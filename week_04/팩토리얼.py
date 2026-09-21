n = 5
f_val = factorial(5)
print(f"{n}의 팩토리얼은 {f_val}입니다.")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    n = 5
    f_val = factorial(5)
    print(f"{n}의 팩토리얼은 {f_val}입니다.")
if __name__ == "__main__":
    main()
