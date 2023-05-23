answer = input("Is it raining ? ")
if answer.lower () == "yes" :
    print("I will stay at home !") # this is the true part of if statement.
    print("Fromm true part") # True part
print("Have a good day !") # This is another statement. Not part of an if statement
finalGrade = float(input(" Enter your final mark : "))
if float(finalGrade) >= 60 :
    print("Congrats ! You passed the course!")
print("From outside the if statement")

billAmount = float(input("Enter the bill amount "))
# We have to add another statement
totalAmount = billAmount
if billAmount < 50 :
    totalAmount = billAmount + 20

print("Your total bill is ", totalAmount)