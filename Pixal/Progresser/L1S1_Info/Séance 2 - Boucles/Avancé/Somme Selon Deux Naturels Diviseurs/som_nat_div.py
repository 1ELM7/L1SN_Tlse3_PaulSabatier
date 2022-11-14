a=int(input())
b=int(input())
count = 0

for i in range (1,1001):
    if (i%a==0) or (i%b==0):
        count = count + i

print (count)
