# Module 13 -- Exception Handling and Debugging

An exception is an error detected while a program runs. Handling
exceptions lets a program respond to expected problems.

## try and except

``` python
try:
    number = int(input("Enter a whole number: "))
    print(10 / number)
except ValueError:
    print("Enter a valid whole number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## else and finally

`else` runs if no exception occurs. `finally` runs whether an exception
occurred or not.

``` python
try:
    value = int("25")
except ValueError:
    print("Invalid")
else:
    print("Converted:", value)
finally:
    print("Finished")
```

## raise

Use `raise` to signal an invalid situation.

``` python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

## Debugging tips

Read the traceback, check the line mentioned, inspect variable values
and test small parts of the program.

## Try it

Handle invalid numeric input, handle division by zero, and raise
`ValueError` for a negative quantity.
