n = 5 # int(input())
k = 2 # int(input())
l = [int(i+1) for i in range(n)]
index = 0
while len(l) != 1:
    index = (index+k-1) % n
    l.pop(index)
    n -= 1
print(l[0])