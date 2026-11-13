# Module 15 -- Comprehensions and Iterators

## List comprehensions

A list comprehension creates a list from an iterable.

``` python
squares = [n * n for n in range(1, 6)]
print(squares)
```

With a condition:

``` python
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)
```

## Dictionary comprehensions

``` python
squares = {n: n * n for n in range(1, 4)}
print(squares)
```

## Iterables and iterators

An iterable can be looped over. An iterator provides values one at a
time using `next()`.

``` python
colours = ["red", "blue"]
iterator = iter(colours)
print(next(iterator))
print(next(iterator))
```

## Generators

A generator function uses `yield` to produce values one at a time.

``` python
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for value in count_up_to(3):
    print(value)
```

## Try it

Create a list of cubes, a dictionary of squares, and a generator that
yields even numbers up to a limit.
