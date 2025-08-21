import datetime

products = {
    "Sugar": 50,
    "Milk": 50,
    "Oil": 50,
    "Bread": 50,
    "Eggs": 50,
    "Banana": 50
}

cart = {}
total = 0

print("Welcome to Kavita Grocery Store")
print("\nAvailable products:")
for item, price in products.items():
    print(f"{item} - ₹{price}")

while True:
    product = input("\nEnter product name to add to cart (or type 'done' to finish): ").title()

    if product == "Done":
        break

    if product in products:
        qty = int(input(f"Enter quantity of {product}: "))
        cart[product] = cart.get(product, 0) + qty
        total += products[product] * qty
        print(f"Added {qty} x {product} to cart.")
    else:
        print("Product not found. Please try again.")

# Bill Receipt
print("\nBill Receipt")
print("-" * 30)
for item, qty in cart.items():
    price = products[item] * qty
    print(f"{item} x {qty} = ₹{price}")

print("-" * 30)
print(f"Total: ₹{total}")

# Apply discount if total > 500
if total > 500:
    discount = total * 0.1
    total -= discount
    print(f"Discount Applied: ₹{discount}")
    print(f"Final Total: ₹{total}")

# Print date & time
print(f"\nDate & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Thank you for shopping with us")
