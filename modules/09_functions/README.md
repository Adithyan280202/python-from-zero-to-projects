# Module 09 -- Functions and Scope

A function is a reusable block of code that runs when called.

``` python
def greet():
    print("Hello!")
greet()
```

## Parameters and arguments

A parameter appears in the function definition; an argument is the value
passed when calling it.

``` python
def greet(name):
    print(f"Hello, {name}!")
greet("Asha")
```

## Return values

`return` sends a result back to the caller.

``` python
def add(a, b):
    return a + b
print(add(5, 3))
```

## Default parameters, \*args and \*\*kwargs

``` python
def welcome(name="friend"):
    print(f"Hello, {name}")

def add_all(*numbers):
    return sum(numbers)

def show_details(**details):
    print(details)
```

A local variable is created inside a function. A global variable is
defined outside functions. Prefer parameters and return values for
sharing data.

## Try it

Write functions to square a number, check whether a number is even, and
calculate a rectangle's area.
