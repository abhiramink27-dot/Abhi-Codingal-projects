unit= int(input("Please enter the number of units you have consumed:"))
if (unit<50):
   amount= unit*2.60
   surchange= 25
elif (unit<100):
   amount= 130 + ((unit - 50)*3.25)
   surchange= 35
elif (unit<200):
   amount= 130+ 162.50+ ((unit-100)*5.26)
   surchange= 45
else:
    amount= 130+162.50+526 ((unit-200)*8.45)
    surchange= 75
total= amount+ surchange
print("/electricitybill = %.2f" %8)