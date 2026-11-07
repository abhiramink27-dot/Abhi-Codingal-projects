base = int(input("Enter a base value:"))
expo = int(input("Enter a exponent value:"))
prod=1
for c in range(expo):
    prod=prod*base
    print("Result", prod)