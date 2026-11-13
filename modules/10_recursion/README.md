# Module 10 -- Recursion and Lambda

## Recursion

Recursion occurs when a function calls itself. It needs a base case to
stop.

``` python
def factorial(n):
    if n == 0:       # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## Lambda

A lambda is a small anonymous function containing one expression.

``` python
square = lambda number: number * number
print(square(4))
```

Use `def` for longer or more complex functions.

## Example -- Sort by length

``` python
names = ["Anu", "Christopher", "Mia"]
print(sorted(names, key=lambda name: len(name)))
```

## Try it

Write a recursive countdown, a recursive sum from 1 to n, and a lambda
that converts Celsius to Fahrenheit.
