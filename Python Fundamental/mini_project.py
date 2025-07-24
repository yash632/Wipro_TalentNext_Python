# Project: 1
# Create a python program that asks the user how far they want to travel. If they want to travel less than
# three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than three
# hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to
# driver Super-Car.
# Tech Module: Python Fundamentals:

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")

#Project: 2
# Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
# You decide to host your application on servers running in the cloud. You pick a hosting provider
# that charges $0.51 per hour. You will launch your service using one server and want to know
# how much it will cost to operate per day,per week,per month.
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per week?
# How much does it cost to operate one server per month?
# How many days can I operate one server with $918?

cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30  

budget = 918
days_operable = budget / cost_per_day

print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for {days_operable:.2f} days")

