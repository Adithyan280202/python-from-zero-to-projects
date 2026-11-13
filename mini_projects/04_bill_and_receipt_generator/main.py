
# Mini Project 04
# Bill and Receipt Generator

print("=" * 45)
print("          BILL GENERATOR")
print("=" * 45)

# Shop information
shop_name = input("Enter shop name: ")
customer_name = input("Enter customer name: ")

# Product 1
print("\nEnter Product 1 Details")
product1 = input("Product name: ")
price1 = float(input("Price per item: "))
quantity1 = int(input("Quantity: "))
total1 = price1 * quantity1

# Product 2
print("\nEnter Product 2 Details")
product2 = input("Product name: ")
price2 = float(input("Price per item: "))
quantity2 = int(input("Quantity: "))
total2 = price2 * quantity2

# Product 3
print("\nEnter Product 3 Details")
product3 = input("Product name: ")
price3 = float(input("Price per item: "))
quantity3 = int(input("Quantity: "))
total3 = price3 * quantity3

# Bill calculations
subtotal = total1 + total2 + total3

discount_percentage = float(input("\nEnter discount percentage: "))
discount = subtotal * discount_percentage / 100

final_amount = subtotal - discount

# Display data types
print("\n" + "=" * 45)
print("              DATA TYPES")
print("=" * 45)

print("Shop Name:", type(shop_name))
print("Customer Name:", type(customer_name))
print("Product Price:", type(price1))
print("Quantity:", type(quantity1))
print("Subtotal:", type(subtotal))
print("Discount:", type(discount))
print("Final Amount:", type(final_amount))

# Generate receipt
print("\n" + "=" * 45)
print(f"          {shop_name.upper()}")
print("=" * 45)

print(f"Customer: {customer_name}")

print("-" * 45)
print(f"{'Product':<15}{'Qty':<6}{'Price':<10}{'Total':<10}")
print("-" * 45)

print(f"{product1:<15}{quantity1:<6}{price1:<10.2f}{total1:<10.2f}")
print(f"{product2:<15}{quantity2:<6}{price2:<10.2f}{total2:<10.2f}")
print(f"{product3:<15}{quantity3:<6}{price3:<10.2f}{total3:<10.2f}")

print("-" * 45)
print(f"{'Subtotal':<30}{subtotal:.2f}")
print(f"{'Discount':<30}{discount:.2f}")
print(f"{'Final Amount':<30}{final_amount:.2f}")
print("=" * 45)

print("        THANK YOU! VISIT AGAIN!")
print("=" * 45)
