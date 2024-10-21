import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Root 1: {root1:.2f}")
    print(f"Root 2: {root2:.2f}")

elif discriminant == 0:
    root = -b / (2*a)    
    print(f"Root: {root:.2f}")

else:
    real_part = -b / (2*a)    
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)    
    print(f"Root 1: {real_part:.2f} + {imaginary_part:.2f}i")
    print(f"Root 1: {real_part:.2f} + {imaginary_part:.2f}i")