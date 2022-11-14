couples=eval(input())
person=str(input())
count = 0

for (couple_un,couple_2) in couples:
    if person==couple_2:
        count+=1

print(count)
