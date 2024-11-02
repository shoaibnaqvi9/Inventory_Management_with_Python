items = {}
def add_product():
    item_key = f"item{len(items) + 1}"
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    category = input("Enter the category of the item: ")
    quantity = int(input("Enter the quantity of the item: "))

    items[item_key] = {
        "name": name,
        "price": price,
        "category": category,
        "quantity": quantity
    }
    print(f"Product '{name}' added successfully!")

def update_product():
    item_key = input("Enter the item key to update (e.g., item1): ")
    if item_key in items:
        print("1. Update price")
        print("2. Update quantity")
        choice = input("Choose an option: ")        
        if choice == "1":
            new_price = float(input("Enter the new price: "))
            items[item_key]["price"] = new_price
            print(f"Price updated for {items[item_key]['name']}.")
        elif choice == "2":
            new_quantity = int(input("Enter the new quantity: "))
            items[item_key]["quantity"] = new_quantity
            print(f"Quantity updated for {items[item_key]['name']}.")
        else:
            print("Invalid choice!")
    else:
        print("Product not found!")

def delete_product():
    item_key = input("Enter the item key to delete (e.g., item1): ")
    if item_key in items:
        deleted_item = items.pop(item_key)
        print(f"Product '{deleted_item['name']}' deleted successfully.")
    else:
        print("Product not found!")

def view_products():
    sorted_items = dict(sorted(items.items(), key=lambda x: x[1]["name"]))
    for key, value in sorted_items.items():
        print(f"{key}: {value}")

def search_product():
    print("1. Search by category")
    print("2. Search by price range")
    choice = input("Choose an option: ")
    if choice == "1":
        category = input("Enter the category to search: ")
        found = False
        for key, value in items.items():
            if value["category"].lower() == category.lower():
                print(f"{key}: {value}")
                found = True
        if not found:
            print("No products found in this category.")
    elif choice == "2":
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        found = False
        for key, value in items.items():
            if min_price <= value["price"] <= max_price:
                print(f"{key}: {value}")
                found = True
        if not found:
            print("No products found in this price range.")
    else:
        print("Invalid choice!")

def save_to_file():
    with open("inventory.txt", "w") as file:
        for key, value in items.items():
            line = f"{key},{value['name']},{value['price']},{value['category']},{value['quantity']}\n"
            file.write(line)
    print("Inventory saved to 'inventory.txt'.")

def load_from_file():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                key, name, price, category, quantity = line.strip().split(",")
                items[key] = {
                    "name": name,
                    "price": float(price),
                    "category": category,
                    "quantity": int(quantity)
                }
        print("Inventory loaded from 'inventory.txt'.")
    except FileNotFoundError:
        print("No saved inventory found.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View All Products")
        print("5. Search Products")
        print("6. Save Inventory to File")
        print("7. Load Inventory from File")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            search_product()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
