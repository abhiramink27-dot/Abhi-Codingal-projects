sp=int(input("Enter your selling price"))
cp=int(input("Enter your cost price"))
if  sp>cp:
 profit= sp-cp
 print("You got a profit of", profit)
else:
    loss= cp-sp
    print("You got a loss of",loss)