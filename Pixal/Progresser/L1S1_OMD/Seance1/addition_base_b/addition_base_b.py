b = int(input())

ka = int(input())
kb = int(input())

k = max(ka, kb)
c1 = [0] * (k+1)
c2 = [0] * (k+1)

for i in range(ka+1):
    c1[i] = int(input())
for i in range (kb+1):
    c2[i] = int(input())

i = 0
r = 0
d = [0] * (k+1)

while (i<=k):
    d[i] = c1[i]+c2[i]+r
    if (d[i]>=b):
        d[i]=d[i]-b
        r=1
    else:
        r=0
    i+=1

if (r==1):
    d.append(r)

print(d)
