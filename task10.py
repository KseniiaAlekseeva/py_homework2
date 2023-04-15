flag = False
while not flag:
    n = int(input("Enter the number of coins: "))
    if n > 0:
        flag = True

count0 = 0
count1 = 0
for i in range(n):
    flag = False
    c = int(input(f"Enter the {i+1} coin: "))
    if c == 0:
        count0 += 1
    if c == 1:
        count1 += 1

if count0 < count1:
    min_c = count0
else:
    min_c = count1

print(f"Minimum {min_c} coins.")
