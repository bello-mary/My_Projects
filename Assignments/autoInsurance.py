# My name is Mary Bello
# My W# is W0451351
# This is my third assignment.

# Input
sex = input("Are you 'Male' or 'Female' : ")
age = int(input("Enter your age : " ))
priceOfVehicle = int(input("Enter the purchase price of the vehicle :" ))


# Process

if sex.lower() == 'male':
    if age >= 15 and age < 25:
        insuranceRate = 0.25
    elif age >= 25 and age < 40:
        insuranceRate = 0.17
    elif age >= 40 and age <70:
        insuranceRate = 0.10

else:
    if age >= 15 and age < 25:
        insuranceRate = 0.20
    elif age >= 25 and age < 40:
        insuranceRate = 0.15
    elif age >= 40 and age <70:
        insuranceRate = 0.10

# Output
monthlyInsuranceAmount = insuranceRate * priceOfVehicle /12
print("Your monthly insurance will be , ${0:.2f}".format(monthlyInsuranceAmount))





