# Module 08 -- Looping Statements

Loops repeat code.

## for loop

A `for` loop visits items in a sequence.

``` python
for fruit in ["apple", "banana", "mango"]:
    print(fruit)
```

## range()

`range(stop)` produces numbers from zero up to, but not including,
`stop`.

``` python
for number in range(1, 6):
    print(number)
```

## while loop

A `while` loop repeats while its condition is true. Update the condition
so the loop can finish.

``` python
count = 1
while count <= 5:
    print(count)
    count += 1
```

## break and continue

`break` exits a loop. `continue` skips to the next iteration.

``` python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

## Nested loops

A nested loop is a loop inside another loop.

``` python
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)
```

## Try it

Print a multiplication table, calculate the sum from 1 to 100, and print
even numbers from 1 to 50.
