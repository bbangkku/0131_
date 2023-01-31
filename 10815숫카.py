from csv import list_dialects
from re import A
from collections import Counter
import sys
sys.stdin = open("./nn.txt","r")

n = int(input())
sangli = list(map(int,input().split()))
tc = int(input())
testli = list(map(int,input().split()))
answer = [0] * tc

for i in range(tc):
    if testli[i] in sangli:
        answer[i] = 1
    else:
        pass

for j in range(tc):
    print(answer[j],end= ' ')