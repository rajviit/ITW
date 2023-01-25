
if __name__ == '__main__':
    z = 1
    stk = []
    top = -1
    print("Perform Oeration")
    print("1 addition of element in stack")
    print("2 remove element from stack")
    print("3 Print the stack elements")
    print("Enter 0 to EXIT")
    while z != 0:
        num = int(input("Enter the operation number you want to perform"))

        if num == 0:
            z = 0

        if num == 1:
            b = int(input("Enter Input :" ))
            stk.append(b)
            stop = top + 1

        elif num == 2:
            stk.pop(top)
            top = top - 1
        elif num == 3:
            print(stk)






