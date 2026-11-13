# Module 04 -- Input and Output

`print()` displays output. `input()` reads text typed by the user.

``` python
name = input("Enter your name: ")
print("Hello", name)
```

`input()` returns a string. Convert it when you need a number:

``` python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

An f-string inserts values into text:

``` python
name = "Maya"
age = 21
print(f"{name} is {age} years old.")
```

## Example -- Bill calculator

``` python
item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity
print(f"{item}: Rs. {total:.2f}")
```

## Try it

Ask for two numbers and display their sum. Then ask for an item price
and quantity and calculate the total.
