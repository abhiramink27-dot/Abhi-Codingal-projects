medical_cause =input("Do you have a medical cause (Y/N):").strip().upper()
if medical_cause== 'Y':
  print("You are allowed")
else:
  attende =int(input("What is the attendence"))
  if attende <=75:
    print("You are allowed")
  else:
    print("You are not allowed")