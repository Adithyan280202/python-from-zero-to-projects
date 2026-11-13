# Module 07 -- Conditional Statements

Conditionals let a program choose which code to run.

## if and else

``` python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## elif

Use `elif` to check another condition when earlier conditions were
false.

``` python
mark = 76
if mark >= 90:
    grade = "A"
elif mark >= 75:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "Needs improvement"
print(grade)
```

Conditions can be combined with `and`, `or` and `not`. Python uses
indentation to define each block.

## Try it

1.  Check whether a number is positive, negative or zero.
2.  Check voting eligibility using 18 as the example age.
3.  Create a grade calculator.
