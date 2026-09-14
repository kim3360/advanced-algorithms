def moveLRUD():
    n = int(input("공간의 크기를 입력하세요: "))
    x, y = 1, 1
    plans = input("이동 계획을 입력하세요: ").split()

    plans_type = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    move_type = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_type)):
            if plan == move_type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
                    x, y = nx, ny
    return x, y

if __name__ == "__main__":
    moveLRUD()
