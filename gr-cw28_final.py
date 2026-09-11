# AINEMBABAZI Meron Keron (Task 1: Menu Setup)
def get_menu():
    # This stores our food and prices, separated by category.
    menu = {
        "Meals": {
            "Matooke": 7000,
            "Pilau": 8000,
            "Cassava": 4000
        },
        "Drinks": {
            "Yoghurt": 3500,
            "Mango Juice": 4000,
            "Water": 2000
        },
        "Snacks": {
            "Fries": 4000,
            "Sausages": 2000,
            "Samosa": 2500
        }
    }
    return menu


# INNOCENT Lubanga-Kene Arop (Task 2: File Persistence)
def save_orders(orders_list):
    # Open the text file to write the new list of orders.
    with open("orders.txt", "w") as file:
        for order in orders_list:
            # Change the order into text and save it on a new line.
            file.write(str(order) + "\n")
    print("Orders saved successfully.")

def load_orders():
    # Try to open the file to read the saved orders.
    try:
        with open("orders.txt", "r") as file:
            saved_data = file.readlines()
        print("Orders loaded successfully.")
        return saved_data
    # If the file is missing, start with an empty list instead of crashing.
    except FileNotFoundError:
        print("No previous orders found. Starting a fresh session.")
        return []


# AMIYA Joan (Task 3: Order Taking)
def calculate_subtotal(cart, menu):
    subtotal = 0

    # Look at each item the customer wants to buy.
    for order_item in cart:
        item_name = order_item.get("name")
        quantity = order_item.get("quantity")
        item_found = False

        # Look through all the categories to find the food's price.
        for category in menu:
            if item_name in menu[category]:
                price = menu[category][item_name]
                item_cost = price * quantity
                subtotal = subtotal + item_cost
                item_found = True
        
        # Print a warning if the food is not on the menu.
        if item_found == False:
            print("Warning: " + item_name + " was skipped because it is not on the menu.")

    return subtotal


# TSHUMA Wiragi Adolphe (Task 4: Delivery Fee)
def calculate_delivery_fee(subtotal, distance_km):
    # Orders of 50,000 UGX or more get free delivery.
    if subtotal >= 50000:
        return 0
    # Short distances cost less.
    elif distance_km <= 2:
        return 1000
    elif distance_km <= 5:
        return 3000
    # Far distances cost the most.
    else:
        return 5000


# Cubaka Mugaruka Pascal (Task 5: Rider Assignment)
def assign_rider(available_riders):
    # Remove the first rider from the available list.
    assigned_rider = available_riders.pop(0)
    # Return their name so they can be given an order.
    return assigned_rider


# Khalifan Nahia (Task 6: Status Tracking)
def update_status(current_status, new_status):
    # Only allow the order to move forward one step at a time.
    if current_status == "Pending" and new_status == "Preparing":
        return True
    elif current_status == "Preparing" and new_status == "Out for Delivery":
        return True
    elif current_status == "Out for Delivery" and new_status == "Delivered":
        return True
    # Stop the order if someone tries to skip a step or go backwards.
    else:
        return False


# Kisaakye Flugensio (Task 7: Sales and Reporting)
def get_daily_revenue(all_orders):
    total_revenue = 0
    # Look at every order we have taken.
    for order in all_orders:
        # Only count the money if the order was successfully delivered.
        if order.get("status") == "Delivered":
            total = order.get("total")
            total_revenue = total_revenue + total
    return total_revenue

def get_best_seller(all_orders):
    # Use an empty dictionary as a scoreboard to count the food items.
    item_counts = {}
    for order in all_orders:
        for item in order.get("items"):
            name = item.get("name")
            quantity = item.get("quantity")
            
            # Add to the score if we have seen this food before.
            if name in item_counts:
                item_counts[name] = item_counts[name] + quantity
            # Start a new score if this is the first time seeing it.
            else:
                item_counts[name] = quantity
                
    # Figure out which food has the highest score.
    best_item = "None"
    highest_sold = 0
    for name in item_counts:
        if item_counts[name] > highest_sold:
            highest_sold = item_counts[name]
            best_item = name
            
    return best_item


# Idola Richard (Task 8: Dashboard)
def get_status_counts(all_orders):
    # Start all the counters at zero.
    pending_count = 0
    preparing_count = 0
    delivery_count = 0
    delivered_count = 0
    
    # Read the status of each order and add 1 to the correct counter.
    for order in all_orders:
        status = order.get("status")
        
        if status == "Pending":
            pending_count = pending_count + 1
        elif status == "Preparing":
            preparing_count = preparing_count + 1
        elif status == "Out for Delivery":
            delivery_count = delivery_count + 1
        elif status == "Delivered":
            delivered_count = delivered_count + 1
            
    # Show the final numbers on the screen.
    print("\n--- Live Dashboard ---")
    print("Pending: " + str(pending_count))
    print("Preparing: " + str(preparing_count))
    print("Out for Delivery: " + str(delivery_count))
    print("Delivered: " + str(delivered_count))


# Tamale Marvin (Task 9: Main Driver Program)
def run_canteen_system():
    print("Starting system...")
    current_orders = load_orders()
    menu = get_menu()
    
    # A list of our local riders ready to work.
    available_riders = ["Kato", "Wasswa", "Mukasa", "Kizito"]
    
    # This loop keeps the menu running until the user chooses to exit.
    while True:
        print("\n=== CAMPUS FOOD DELIVERY ===")
        print("1. View Menu")
        print("2. Place a New Order")
        print("3. Assign Rider to a Pending Order")
        print("4. View Live Dashboard")
        print("5. View Sales Report")
        print("6. Save and Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print("\n--- CANTEEN MENU ---")
            for category in menu:
                print("\n" + category + ":")
                for item in menu[category]:
                    print("- " + item + ": " + str(menu[category][item]) + " UGX")
            
        elif choice == "2":
            print("\n--- BUILD AN ORDER ---")
            
            # Put all food items into a simple numbered list to make ordering easy.
            numbered_menu = []
            for category in menu:
                for item in menu[category]:
                    numbered_menu.append(item)
            
            # Show the numbered menu to the customer.
            for index in range(len(numbered_menu)):
                print(str(index + 1) + ". " + numbered_menu[index])
                
            cart = []
            while True:
                # Ask the customer to type a number, or just press Enter to stop.
                food_choice = input("\nEnter item number (or press Enter to finish): ")
                
                if food_choice == "":
                    break
                
                # Check if the customer actually typed a number.
                if food_choice.isdigit():
                    index = int(food_choice) - 1
                    
                    # Make sure the number matches something on the menu.
                    if 0 <= index < len(numbered_menu):
                        selected_food = numbered_menu[index]
                        qty = int(input("Enter quantity for " + selected_food + ": "))
                        cart.append({"name": selected_food, "quantity": qty})
                        print(selected_food + " added to cart!")
                    else:
                        print("Invalid number. Please pick a number from the menu.")
                else:
                    print("Please enter a number.")
            
            # Cancel the order if they did not pick any food.
            if len(cart) == 0:
                print("Cart is empty. Order cancelled.")
            else:
                distance = int(input("\nEnter delivery distance in km: "))
                
                # Calculate the costs.
                sub = calculate_subtotal(cart, menu)
                fee = calculate_delivery_fee(sub, distance)
                total = sub + fee
                
                # Build the complete order details.
                new_order = {
                    "order_number": len(current_orders) + 1,
                    "customer": "Student",
                    "subtotal": sub,
                    "delivery_fee": fee,
                    "total": total,
                    "rider": "",
                    "status": "Pending",
                    "items": cart
                }
                current_orders.append(new_order)
                print("\nOrder placed! Total cost: " + str(total) + " UGX")
            
        elif choice == "3":
            print("\n--- ASSIGN RIDER ---")
            if len(available_riders) == 0:
                print("No riders available right now!")
            else:
                order_assigned = False
                # Look for the first order that is still waiting.
                for order in current_orders:
                    if order.get("status") == "Pending":
                        rider_name = assign_rider(available_riders)
                        order["rider"] = rider_name
                        
                        update_status(order["status"], "Preparing")
                        order["status"] = "Preparing"
                        
                        print("Order #" + str(order["order_number"]) + " assigned to " + rider_name + ".")
                        order_assigned = True
                        break
                
                if order_assigned == False:
                     print("There are no pending orders right now.")
                        
        elif choice == "4":
            get_status_counts(current_orders)
            
        elif choice == "5":
            print("\n--- SALES REPORT ---")
            revenue = get_daily_revenue(current_orders)
            best_item = get_best_seller(current_orders)
            print("Total Daily Revenue: " + str(revenue) + " UGX")
            print("Best-Selling Item: " + str(best_item))
            
        elif choice == "6":
            # Save all the work to the text file and stop the loop.
            save_orders(current_orders)
            print("Shutting down. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please type a number between 1 and 6.")

# This command starts the whole program.
if __name__ == "__main__":
    run_canteen_system()