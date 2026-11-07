num = int(input("Enter the number of your choice:"))


sum = 0 

temp = num
while temp > 0:
    digit = temp % 10
    sum+= digit **3
    temp //= 10

if num== sum:
    print(num,"Is an Armstrong number.")
else:
    print(num,"Is not a Armstrong number.")