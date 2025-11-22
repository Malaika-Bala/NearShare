item_name = []
owner_name = []
contact_number = []
category = []
price = []

def add_item():
    print("\n--- Add New Item ---")
    name = input("Enter Item Name: ")
    owner = input("Enter Owner Name: ")
    contact = input("Enter Contact Number: ")
    cat = input("Enter Category (borrow/sell): ")

    if cat.lower() == "sell":
        item_price = float(input("Enter Price: "))
    else:
        item_price = 0

    item_name.append(name)
    owner_name.append(owner)
    contact_number.append(contact)
    category.append(cat)
    price.append(item_price)

    print("Item added successfully!")


def view_items():
    print("\n--- All Listed Items ---")

    if len(item_name) == 0:
        print("No items available.")
        return

    for i in range(len(item_name)):
        print("\n-------------------------")
        print("Item Name :", item_name[i])
        print("Owner     :", owner_name[i])
        print("Contact   :", contact_number[i])
        print("Category  :", category[i])

        if category[i].lower() == "sell":
            print("Price     :", price[i])
        else:
            print("Price     : Not Applicable")


def search_item():
    print("\n--- Search Item ---")
    name = input("Enter item name to search: ")

    found = False

    for i in range(len(item_name)):
        if item_name[i].lower() == name.lower():
            print("\nItem Found:")
            print("-------------------------")
            print("Item Name :", item_name[i])
            print("Owner     :", owner_name[i])
            print("Contact   :", contact_number[i])
            print("Category  :", category[i])

            if category[i].lower() == "sell":
                print("Price     :", price[i])

            found = True

    if not found:
        print("Item not found!")


def main():
    while True:
        print("\n===== NeighbourShare App =====")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            print("Thank you for using the app!")
            break
        else:
            print("Invalid choice! Please try again.")

main()