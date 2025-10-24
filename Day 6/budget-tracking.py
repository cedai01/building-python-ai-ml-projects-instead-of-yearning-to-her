import numpy as np
from IPython.display import Image, display

expenses = np.array([], dtype=int)
budget = np.array([], dtype=object)

def user_expenses():
    user_expensess = int(input("How much did you spend today? "))
    global expenses
    expenses = np.append(expenses, user_expensess)

def user_budget():
    item = input("What's the thing that you want to have a budget? ")
    user_budget = int(input(f"What's your budget for {item}? "))
    return {"item": item, "budget": user_budget}

while True:
    user_expenses()
    user_extra = input("Do you want to add more? Y/N ").upper()
    
    if user_extra != "N":
        budget = np.append(budget, user_budget())
        continue
    else:
        total_expenses = np.sum(expenses)
        
        # collect all the budget values from dictionaries
        tota_budget = sum(sb["budget"] for sb in budget)

        print(f"\nTotal Expenses: {total_expenses}")
        print(f"Total Budget: {tota_budget}\n")

        if total_expenses > tota_budget:
            print(f"You exceeded your budget of {tota_budget}")
            display(Image(filename="Day 6/brokeass.jpg"))
        elif total_expenses < tota_budget:
            print("Congrats you didn't exceed your budget!")
            display(Image(filename="Day 6/congrats.jpg"))
        elif total_expenses == tota_budget:
            print("Ahhhh.... so so, Better get your finances good my lil bro")
            display(Image(filename="Day 6/ref.jpg"))
        else:
            print("Fix this shit nigga! You wrote trash code")
            display(Image(filename="Day 6/tap.jpg"))
        break


