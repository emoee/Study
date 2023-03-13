s = list(input().upper())
lst = []
cnt = cnt2 = 0
for i in range(26):
    lst.append(s.count(chr(ord('A')+i)))
    
for i in range(len(lst)):    
    m = max(lst)
    if m == lst[i]:
        cnt += 1
        cnt2 = i

if cnt == 1:
    print(chr(ord('A')+cnt2))
else:
    print("?")