# Module 16 -- Advanced Core Python

## Decorators

A decorator takes a function and returns a function that adds or changes
behaviour.

``` python
def announce(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@announce
def greet():
    print("Hello!")

greet()
```

`@announce` is shorthand for `greet = announce(greet)`.

For reusable decorators, `functools.wraps` preserves function metadata.

``` python
from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running...")
        return func(*args, **kwargs)
    return wrapper
```

## Context managers

A context manager handles setup and cleanup around a block.
`with open(...)` is a common example.

``` python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

## Useful built-ins

``` python
values = [4, 1, 8]
print(sorted(values))
print(sum(values))
print(max(values))
print(min(values))
```

## Try it

Write a decorator that prints before a function runs. Extend it to
support arguments. Use `with` to write and read a file.
