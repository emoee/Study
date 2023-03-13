import sys
while(1):
    text = input()
    s = []
    test = True
    if text == '.':
        break
    for i in text:
        if i == "(" or i == "[":
            s.append(i)
        elif i == ")":
            if len(s) != 0 and s[-1] == "(":
                s.pop()
            else:
                test = False
        elif i == "]":
            if len(s) != 0 and s[-1] == "[":
                s.pop()
            else:
                test = False
    if len(s) != 0:
        test = False
    if test == True:
        print("yes")
    else:
        print("no")