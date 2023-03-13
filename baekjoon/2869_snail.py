import sys

a, b, v = map(int, sys.stdin.readline().split())
# a 올라가는 높이 b는 내려가는 높이 v는 총 길이
print((v-a-1) // (a-b) +2)