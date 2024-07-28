def display_menu():
    print("Menu:")
    print("1. View menu item")
    print("2. Add menu item")
    print("3. Edit menu item")
    print("4. Delete menu item")
    print("5. Search for ingredient")
    print("6. Exit")

def display_item(menu_dict):
    print("\nMenu Items:")
    for item in menu_dict:
        print(f"Item: {item}, Price: {menu_dict[item]['price']}, Ingredients: {', '.join(menu_dict[item]['ingredients'])}, Calories: {menu_dict[item]['calories']}")
    item_name = input("Enter a menu item name: ")
    if item_name in menu_dict:
        print(f"Item: {item_name}, Price: {menu_dict[item_name]['price']}, Ingredients: {', '.join(menu_dict[item_name]['ingredients'])}, Calories: {menu_dict[item_name]['calories']}")
    else:
        print("Invalid item name. Please try again.")

def add_item(menu_dict):
    item_name = input("Enter the name of the menu item: ")
    if item_name in menu_dict:
        print("This item already exists. Please try again.")
    else:
        price = float(input("Enter the price of the item: "))
        ingredients = input("Enter the ingredients of the item (separated by commas): ").split(',')
        calories = int(input("Enter the number of calories: "))
        menu_dict[item_name] = {'price': price, 'ingredients': ingredients, 'calories': calories}
        print(f"Menu item '{item_name}' has been added.")

def edit_item(menu_dict):
    item_name = input("Enter the name of the menu item you want to edit: ")
    if item_name in menu_dict:
        price = float(input("Enter the new price of the item: "))
        ingredients = input("Enter the new ingredients of the item (separated by commas): ").split(',')
        calories = int(input("Enter the new number of calories: "))
        menu_dict[item_name] = {'price': price, 'ingredients': ingredients, 'calories': calories}
        print(f"Menu item '{item_name}' has been updated.")
    else:
        print("Invalid item name. Please try again.")

def delete_item(menu_dict):
    item_name = input("Enter the name of the menu item you want to delete: ")
    if item_name in menu_dict:
        print(f"Menu item '{item_name}' has been deleted.")
        del menu_dict[item_name]
    else:
        print("Invalid item name. Please try again.")

def search_ingredient(menu_dict):
    ingredient = input("Enter the ingredient you want to search for: ")
    found = False
    for item in menu_dict:
        if ingredient in menu_dict[item]['ingredients']:
            print(f"{item} contains {ingredient}.")
            found = True
    if not found:
        print(f"No menu items contain {ingredient}.")

def main():
    menu_dict = {
        "Burger": {"price": 5.99, "ingredients": ["Bun", "Patty", "Cheese", "Lettuce"], "calories": 250},
        "Pizza": {"price": 7.99, "ingredients": ["Dough", "Tomato Sauce", "Cheese"], "calories": 300},
        "Pasta": {"price": 6.99, "ingredients": ["Pasta", "Tomato Sauce", "Cheese"], "calories": 200}
    }

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_item(menu_dict)
        elif choice == "2":
            add_item(menu_dict)
        elif choice == "3":
            edit_item(menu_dict)
        elif choice == "4":
            delete_item(menu_dict)
        elif choice == "5":
            search_ingredient(menu_dict)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")

        print()

if __name__ == "__main__":
    main()
