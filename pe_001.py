x = range(1000)
y = 0
for n in x:
    if((n % 3 == 0) or (n % 5 == 0)):
        y = y + n

print(y)
