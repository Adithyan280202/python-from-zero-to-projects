# Mini Project 04: Bill and Receipt Generator

## 1. Project Overview

The Bill and Receipt Generator is a beginner-friendly Python project that collects shop, customer, and product information to generate a formatted shopping receipt.

The program accepts three products, calculates the individual product totals, finds the subtotal, calculates a discount, and displays the final bill amount.

This project helps beginners understand how Python can be used for practical calculations in real-world applications.

## 2. Learning Objectives

By completing this project, you will learn:

- How to collect information using `input()`.
- How to store information using variables.
- How to work with strings, integers, and floating-point numbers.
- How to perform arithmetic calculations.
- How to calculate percentages and discounts.
- How to format output using f-strings.
- How to align text using string formatting.
- How to display decimal values using `.2f`.
- How to identify data types using `type()`.

## 3. Project Requirements

The program should:

1. Ask for the shop name.
2. Ask for the customer's name.
3. Collect details of three products.
4. Ask for each product's price and quantity.
5. Calculate the total price of each product.
6. Calculate the subtotal of all products.
7. Ask for the discount percentage.
8. Calculate the discount amount.
9. Calculate the final bill amount.
10. Display the data types of selected variables.
11. Generate a formatted shopping receipt.

**Important:** Complete this project without conditional statements or loops.

## 4. Information to Collect

| Information | Data Type |
|---|---|
| Shop Name | String (`str`) |
| Customer Name | String (`str`) |
| Product Name | String (`str`) |
| Product Price | Float (`float`) |
| Product Quantity | Integer (`int`) |
| Discount Percentage | Float (`float`) |

## 5. Calculation Formulas

### Product Total

`Product Total = Price × Quantity`

### Subtotal

`Subtotal = Product 1 Total + Product 2 Total + Product 3 Total`

### Discount Amount

`Discount = Subtotal × Discount Percentage / 100`

### Final Bill Amount

`Final Amount = Subtotal - Discount`

## 6. Sample Input

```text
Enter shop name: Tech Store
Enter customer name: Rahul

Product 1:
Product name: Keyboard
Price per item: 800
Quantity: 2

Product 2:
Product name: Mouse
Price per item: 400
Quantity: 1

Product 3:
Product name: USB Cable
Price per item: 150
Quantity: 3

Enter discount percentage: 10
```

## 7. Expected Calculation

| Product | Quantity | Price | Total |
|---|---:|---:|---:|
| Keyboard | 2 | 800 | 1600 |
| Mouse | 1 | 400 | 400 |
| USB Cable | 3 | 150 | 450 |
| **Subtotal** | | | **2450** |

**Discount calculation:**

- Subtotal = ₹2,450
- Discount percentage = 10%
- Discount amount = ₹245
- Final amount = ₹2,205

## 8. Expected Output

```text
=============================================
                 TECH STORE
=============================================

Customer: Rahul

Product         Qty   Price     Total
---------------------------------------------
Keyboard        2     800.00    1600.00
Mouse           1     400.00    400.00
USB Cable       3     150.00    450.00
---------------------------------------------
Subtotal                       2450.00
Discount                        245.00
Final Amount                   2205.00
=============================================
        THANK YOU! VISIT AGAIN!
=============================================
```

## 9. Concepts Used

### Variables
Variables store shop details, customer information, product details, and calculation results.

### Input Function
The `input()` function collects information from the user.

### Data Types
- `str` – Stores text.
- `int` – Stores whole numbers.
- `float` – Stores decimal numbers.

### Type Conversion
- `int()` converts input into an integer.
- `float()` converts input into a floating-point number.

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

### Percentage Calculation
Percentage calculations are used to find the discount amount.

### f-Strings
f-strings allow variables to be inserted directly into formatted output.

### String Alignment

The formatting expression `<30` aligns text to the left within a 30-character space.

### Decimal Formatting

The formatting expression `.2f` displays a floating-point number with exactly two digits after the decimal point.

### Type Function

The `type()` function identifies the data type of a variable.

## 10. Practice Challenges

Try improving the program by completing these tasks:

1. Add two more products.
2. Add GST calculation.
3. Ask the customer for the amount paid.
4. Calculate the balance to return.
5. Add the shop address and phone number.
6. Display all prices with two decimal places.
7. Add a receipt number.
8. Improve the receipt design.

## 11. How to Run the Project

Make sure Python is installed on your computer.

Open the project folder in VS Code and execute:

```bash
python main.py
```

**Note:** Enter a non-negative discount percentage. This version uses a non-zero number of products and does not include input validation.

## 12. Project Structure

```text
04_bill_and_receipt_generator/
│
├── README.md
└── main.py
```

## 13. Learning Outcome

After completing this project, you should be able to collect product information, perform price and percentage calculations, work with different data types, and generate a formatted shopping receipt using Python.

---

**Part of Python From Zero to Projects**

A beginner-friendly, project-based Python learning journey.
