def twoDExample():
    # for i in range(0, 5):
    #     for j in range(0, 5):
    #         print(f"({i}, {j})", end=" ")
    #     print()


    # 동, 북, 서, 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    x, y = 2, 2

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            print(f"({nx}, {ny})", end=" ")
    print()

if __name__ == "__main__":
    twoDExample()
