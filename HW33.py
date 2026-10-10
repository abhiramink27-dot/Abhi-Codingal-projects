print("Enter marks optained in 4 subjects")
English= int(input("english :"))
Math= int(input("maths :"))
Science= int(input("science : "))
SocialStudies=int(input("Social Studies : "))

sum= English+Math+Science+SocialStudies
print("The sum of English, Math, Science, and SocialStudies is:", sum)

per=(sum/400)*100
print("The percentage mark is:",per)