for i in range(0, 151):
    print(i)

for i in range(0, 1001, 5):
    print(i)

for i in range(0,101):
    if i % 10 == 0: print("coding dojo")
    elif i % 5 == 0: print("coding")
    else:
        print(i)

sum = 0
for i in range(1,500001,2):
    sum += i
    print(i)

for i in range(2018, -1, -4):
    print(i)

low = 2
high = 18
mult = 2

for i in range(low, high + 1):
    if i % mult ==0:
        print(i)