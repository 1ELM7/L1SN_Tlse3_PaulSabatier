u = int(input())
d = int(input())
r = 0

y = 0
z = min(u,d)
i = 0

while (i < z):
    y = y+max(u,d)
    i += 1

print (y)
