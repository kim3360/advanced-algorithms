def stackExample():
    stack = []
    stack.append(5)
    stack.append(4)
    stack.append(3)
    stack.append(2)
    print(stack)


    popData = stack.pop()
    print(popData)
    print(stack)

    stack.append(1)
    print(stack)

if __name__ == "__main__":
    stackExample()
