import sys
sys.stdin = open("./nn.txt","r")

n, k = map(int,input().split())
num = list(map(int,input()))
answer = []
for i in range(n-k):
    answer.append(num[i])    
    if answer[i] <= num[i+1]:
        answer.pop()
        answer.append(num[i+1])  
    # else:


    # print(max(num[i:n-k+i]))


