def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    a = 10
    b = 5
    print(gcd(a, b))
