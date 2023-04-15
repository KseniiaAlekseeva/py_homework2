# x < 1000
# y < 1000

# s < 2000
# p < 1000000

# x+y = s
# x*y = p

# y = s-x
# x*(s-x) = p
# x^2-sx+p = 0
# y=s-x

import math

s = int(input("Enter the sum of numbers S (<=2000): "))
p = int(input("Enter the multiplication of numbers P (<=1000000): "))

D = s*s-4*p
print(f"D={D}")

if D >= 0:
    x1 = (s+math.sqrt(D))/2
    x2 = (s-math.sqrt(D))/2
    print(f"x1={x1}, x2={x2}")

    isint1 = float(x1).is_integer()

    if x1 > 0 and isint1:
        x = int(x1)
        y = s-x
        print(f"x={x}, y={y}")
    else:
        print("No solution in integer numbers.")

else:
    print("No solution in real numbers.")
