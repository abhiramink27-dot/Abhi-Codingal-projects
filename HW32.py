Amount =int(input("Please enter amount for withdraw:"))
note_1= Amount/100
note_2= (Amount%100)//50
note_3= ((Amount%100)/50)//10
print("The notes of 100 rupee:"note_1)
print("The notes of 50 rupeee:"note_2)
print("The notes of 10 rupee:"note_3)