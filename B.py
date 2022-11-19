lst = list(map(int,input().split()))
if sum(lst) == 180:
    print(max(lst))
else:
    print(-1)