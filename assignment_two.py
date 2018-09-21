
# Yerim-Oumar Dia
# Intro to Computer Science
# Last modified : September 11,2018
# Car Payment Chatbot :
# This chatbot is designed to find the average monthly car payments and the total price.
# As the user inputs different values, the chatbot will calculate and react accordingly.

name = input("Hello, what is your name?")
print("Hello", name, " That's a very nice name")
print("By the way my name is Yemo and I will be your chatbot for today")
location = input("Where are you from?")
print("Wow", location, "That is an awesome place to be from")
user_favorite_number = input("What is your favorite number?")
favorite_number = float(user_favorite_number) * float(3)
print("My favorite number is:", favorite_number)
favorite_car = input("What is your dream car")
print("A", favorite_car, "you sure have some luxury tastes")
car_choice = input("Why is this your favorite car?")
print("Well I have to admit it is an extremely beautiful car")
price = float(input("And what is the base price of the car?"))
print("Geez", price, "that is very expensive")
car_years = float(input("How many years of loans are you planning on taking?"))
# car_years = amount of years for the loan
rate = float(input("And what interest rate have you been able to find?"))
rate = rate / 100 / 12
# mutltiply divide rate by 100 then by 12
monthly_payment = (rate * price) / (1 - (1 + rate) ** (-car_years * 12))
print(" Well your monthly payment will be ", monthly_payment, "I hope that will be suitable for your budget ")
total_payment = (monthly_payment * car_years * 12)
print(" Well after my calculations your total price for your dream car would be", total_payment)
satisfied = input("Are you happy with these results?")
print("Well", name, "I hope I have been a good help to you, and best of wishes with your dream car")
