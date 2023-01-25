print("1 To perform Stack")
print("2 To perform Queue")
op = int(input("Enter :" ))
if op == 1:
    z = 1
    stk = []
    top = -1
    print("Perform Operation")
    print("1 addition of element in stack")
    print("2 remove element from stack")
    print("3 Print the stack elements")
    print("Enter 0 to EXIT")
    while z != 0:
        num = int(input("Enter the operation number you want to perform : "))

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
else:
    r = 1
    que = []
    front = 0
    rear = 0
    print("Perform Operation")
    print("1 addition of element in queue")
    print("2 remove element from queue")
    print("3 Print the queue elements")
    print("Enter 0 to EXIT")
    while r != 0:
        x = int(input("Enter the operation number you want to perform : "))

        if x == 0:
            r = 0

        if x == 1:
            p = int(input("Enter Input :"))
            que.append(p)
            rear = rear + 1

        elif x == 2:
            que.pop(front)
            front = front + 1
        elif x == 3:
            print(que)







