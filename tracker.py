# Name - Vipin Tanwar
# Date: 2025-10-06
# Project: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")
print("This tool helps you log your meals and calories, compare against your daily limit, and save your session.\n")

meal_names = []
calorie_amounts = []

num_meals = int(input("How many meals do you want to enter today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name: ")
    calories = float(input("Enter calorie amount: "))
        
    meal_names.append(meal)
    calorie_amounts.append(calories)
    
total_calories = sum(calorie_amounts)
avg_calories = total_calories/num_meals
daily_limit = float(input("Enter your daily calorie limit"))

if total_calories > daily_limit:
    
    print("Warning:You've exceeded your daily calorie limit.!")
    print(f"You consumed{total_calories - daily_limit} calories extra today.")
else:
    print("Great job! You're within your daily calorie limit.")
    print("You still have{daily_limit - total_calories} calories left.")
    
    print("\n\n--- Daily Calorie Summary ---")
print("Meal Name\tCalories")
print("-" * 30)

for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")

print("-" * 30)
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{avg_calories}")