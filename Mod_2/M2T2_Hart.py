# Create an interactive program where a customer is greeted by name.
print("What is your name: ")

user_name = input()
print()

# - Advertise to the customer the name of the widget, their unit price, and the overall stock on hand.
print(f"Hello {user_name}, today we a sale on WidgetCSC. We have in stock 100 WidgetCSC. Each is worth $4.89 dollars.")

# - Ask the user how many widgets they wish to buy.
print("How many would  you like to purchase")
user_qt = int(input())
print()

print(f"You have asked for {user_qt}")

# - Tell them the gross price (without taxes, etc.)
print(f"Your today cost will be {round((user_qt * 4.89),2)}")
print()

# - Thank them for their business.
print("Thank you for shopping at PetSmart")




