import datetime

# Define the veg menu
veg_menu = {1: ["Veg Biryani", 150], 2: ["Veg Fried Rice", 120], 3: ["Veg Curry", 100], 4: ["Salad", 50]}

# Define the non-veg menu
non_veg_menu = {1: ["Chicken Biryani", 200], 2: ["Chicken Fried Rice", 180], 3: ["Butter Chicken", 250], 4: ["Fish Curry", 220]}

# Display the menus
print("Welcome to Our Restaurant!")
print("---------------------------")
print("Menu:")
print("1. Veg")
print("2. Non-Veg")

# Get the user's menu choice
menu_choice = int(input("\nPlease select the menu: "))

# Display the selected menu
if menu_choice == 1:
    print("\nVeg Menu:")
    for item in veg_menu.items():
        print(f"{item[0]}. {item[1][0]} - {item[1][1]} INR")
elif menu_choice == 2:
    print("\nNon-Veg Menu:")
    for item in non_veg_menu.items():
        print(f"{item[0]}. {item[1][0]} - {item[1][1]} INR")
else:
    print("Invalid choice! Please try again.")

# Get the user's details and order
name = input("\nPlease enter your name: ")
phone = input("Please enter your phone number: ")
order_input = input("Please select the items you want to order (separated by comma): ")
order = list(map(int, order_input.split(",")))
selected_menu = veg_menu if menu_choice == 1 else non_veg_menu

# Get the current date and time
now = datetime.datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

# Calculate the total bill
total = sum([selected_menu[item][1] for item in order if item in selected_menu])

# Display the bill
if total > 0:
    selected_items = {f"{selected_menu[item][0]} - {selected_menu[item][1]} INR" for item in order if item in selected_menu}
    print("\nOrder Details:")
    for item in selected_items:
        print(item)
        
    print(f"\nDate: {dt_string}")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"\nTotal Bill: {total} INR\n")
    print("Thank you for dining with us!")
