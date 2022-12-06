n = int(input())
count = 0 

a = 1000 - n

Yen = [500, 100, 50, 10, 5, 1]

for don in Yen:
    count += a // don
    a %= don

print(count)