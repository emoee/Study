import sys
class Stack :
    def __init__(self):
        self.list = []
    def push(self,x):
        self.list.append(x)

    def pop(self):
        if len(self.list) == 0:
            print(-1)
        else:
            print(self.list.pop(-1))
    def size(self):
        print(len(self.list))
    def empty(self):
        if len(self.list) == 0:
            print(1)
        else:
            print(0)
    def top(self):
        if len(self.list) == 0:
            print(-1)
        else:
            print(self.list[-1])

S = Stack()
a = int(sys.stdin.readline()) #sys.stdin.readline() 입력받는 빠른 방법
for i in range(a):
    test = list(map(str,sys.stdin.readline().split()))
    if test[0] == "push":
        S.push(int(test[1]))
    elif test[0] == "top":
        S.top()
    elif test[0] == "size":
        S.size()
    elif test[0] == "empty":
        S.empty()
    elif test[0] == "pop":
        S.pop()
