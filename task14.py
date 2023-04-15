# 2^k < N

n = int(input("Enter the integer N: "))

k = 0
num = 1

while num <= n:
    print(f"k = {k}, 2^k = {num}")
    k += 1
    num = 2**k
