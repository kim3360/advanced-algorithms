def main():
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    for plan in plans:
        if plan == 'L' and y > 1:
            y -= 1
        elif plan == 'R' and y < n:
            y += 1
        elif plan == 'U' and x > 1:
            x -= 1
        elif plan == 'D' and x < n:
            x += 1
    print(x, y)
    return x, y

def main2():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1,1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                x, y = nx, ny
    print(x, y)
    return x, y

if __name__ == "__main__":
    main()
    # 5
    # R R R U D D
