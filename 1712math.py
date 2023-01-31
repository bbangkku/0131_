from csv import list_dialects
from re import A
from collections import Counter
import sys
sys.stdin = open("./nn.txt")

# n = int(sys.stdin.readline())
# stack = []
# answer = [0] * n
# numli = [input().split() for i in range(n)]
# print(numli)

a, b, c =map(int,input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)


