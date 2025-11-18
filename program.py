import datetime

inventory = {
    "Sugar": 40,
    "Bread": 25,
    "Milk": 30,
    "Eggs": 6,
    "Rice": 60,
    "Soap": 18,
    "Chips": 10
}

def display_products():
    print("\n--- AVAILABLE PRODUCTS ---")
    print(f"{'Item':<15} {'Price (Rs)':<10}")
    print("-" * 25)
    for item, price in inventory.items():
        print(f"{item:<15} {price:<10}")
    print("-" * 25)

def generate_bill(cart_items):
    if not cart_items:
        print("\nCart is empty. No bill generated.")
        return

    print("\n" + "=" * 40)
    print("      SUPERMARKET BILL RECEIPT      ")
    print(f" Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)
    print(f"{'Item':<15} {'Qty':<5} {'Price':<8} {'Total'}")
    print("-" * 40)

    grand_total = 0

    for item, qty, price in cart_items:
        item_total = qty * price
        grand_total += item_total
        print(f"{item:<15} {qty:<5} {price:<8} {item_total}")

    print("-" * 40)
    print(f"GRAND TOTAL: Rs. {grand_total:.2f}")
    print("=" * 40)
    print("Thank you for shopping!\n")

def main():
    cart = []
    
    print("Welcome to the Supermarket System")
    
    while True:
        print("\n1. View Products")
        print("2. Add Item to Cart")
        print("3. Generate Bill & Exit")
        print("4. Exit without Buying")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            display_products()

        elif choice == '2':
            display_products()
            item_name = input("Enter Item Name (Case Sensitive): ").strip()
            
            if item_name in inventory:
                qty_input_valid = False
                while not qty_input_valid:
                    qty_str = input(f"Enter Quantity for {item_name}: ")
                    
                    if qty_str.isdigit():
                        qty = int(qty_str)
                        if qty > 0:
                            price = inventory[item_name]
                            cart.append((item_name, qty, price))
                            print(f"--> Added {qty} x {item_name} to cart.")
                            qty_input_valid = True
                        else:
                            print("Quantity must be greater than 0.")
                    else:
                        print("Invalid input! Quantity must be a whole number.")
            else:
                print("Error: Item not found in inventory.")

        elif choice == '3':
            generate_bill(cart)
            break

        elif choice == '4':
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
