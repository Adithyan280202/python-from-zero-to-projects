# Python Workshop

This document is a text-based version of the uploaded **Python
Workshop** presentation.

## About Python

Python is a versatile and beginner-friendly programming language.

-   It is a user-friendly programming language.
-   Python is known for its clear syntax and readability.
-   Python's syntax is designed to be readable and straightforward,
    making it easy to understand and maintain.
-   Python code is executed line by line, which makes debugging easier
    and faster.
-   Python has a large standard library that includes modules and
    packages for various tasks, from file I/O to web development.
-   Python is popular in web development, data science, and machine
    learning.

## Variables, Keywords, Data Types and Operators

### Variables

Variables in Python store information that can be referenced and
manipulated in a program.

They are created by assigning a value to a name using the `=` operator.

### Keywords

Keywords in Python are reserved words that have special meanings and are
used to define the syntax and structure of the Python language.

These keywords cannot be used as identifiers, such as variable names or
function names.

### Data Types

Python has several built-in data types, each serving different purposes.

**Numeric types:** - `int` - `float` - `complex`

**Text type:** - `str`

### Operators

Operators perform operations on variables and values.

Python supports a wide range of operators, including:

-   **Arithmetic:** `+`, `-`, `*`, `/`, `//`, `%`
-   **Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`
-   **Logical:** `and`, `or`, `not`
-   **Bitwise operators**

## Data Collections

  -----------------------------------------------------------------------
  Data structure          Description             Mutability
  ----------------------- ----------------------- -----------------------
  Lists                   Ordered collections of  Mutable
                          items. Can be modified  
                          after creation.         

  Tuples                  Ordered collections of  Immutable
                          items. Cannot be        
                          modified after          
                          creation.               

  Dictionaries            Collections of          Mutable
                          key-value pairs. Keys   
                          must be unique.         
  -----------------------------------------------------------------------

## Strings

Strings in Python are collections of characters surrounded by either
single or double quotation marks.

Example:

``` python
'hello'
```

is the same as:

``` python
"hello"
```

### String operations

**Multiline strings**

``` python
"""This is a
multiline string."""
```

**String length**

``` python
len(x)
```

**Slicing**

``` python
x[2:5]
```

**Indexing**

Strings support indexing to access individual characters.

### More string operations

**Type**

``` python
type(x)
```

**Uppercase**

``` python
x.upper()
```

**Lowercase**

``` python
x.lower()
```

**Strip**

``` python
x.strip()
```

**Replace**

``` python
x.replace("y", "x")
```

**Concatenation**

Strings can be joined together using concatenation.

## Lists

A list is a data structure in Python that is a mutable, or changeable,
ordered sequence of elements. Lists are used to store multiple items in
a single variable.

### List operations

**Length**

``` python
len(x)
```

**Type**

``` python
type(x)
```

**Slicing**

``` python
x[2:5]
```

**Indexing and accessing items**

``` python
x[1]
```

**Changing items**

``` python
x[1] = "y"
x[1:3] = ["y", "z"]
```

### More list operations

**Append**

``` python
x.append("y")
```

**Insert**

``` python
x.insert(1, "y")
```

**Extend**

``` python
x.extend(y)
```

**Remove**

``` python
x.remove("y")
```

**Pop**

``` python
x.pop(1)
```

**Sort**

``` python
x.sort()
x.sort(reverse=True)
```

## Dictionaries

In Python, dictionaries are mutable data structures that allow you to
store key-value pairs.

A dictionary can be created using the `dict()` constructor or curly
braces `{}`. Dictionaries are used to store data values in key-value
pairs.

### Dictionary operations

**Length**

``` python
len(x)
```

**Accessing items --- get keys**

``` python
x = y.keys()
```

**Accessing items --- get values**

``` python
x = y.values()
```

**Change values**

``` python
x["key"] = value
```

**Update**

``` python
x.update({"key": value})
```

**Pop**

``` python
x.pop("key")
```

**Pop item**

``` python
x.popitem()
```

## Conditional Statements

Python supports the usual logical conditions from mathematics:

  Condition                  Operator
  -------------------------- ----------
  Equals                     `a == b`
  Not equals                 `a != b`
  Less than                  `a < b`
  Less than or equal to      `a <= b`
  Greater than               `a > b`
  Greater than or equal to   `a >= b`

### If

``` python
if x > y:
    # statements
```

### Elif

``` python
elif x > y:
    # statements
```

### Else

``` python
else:
    # statements
```

## Loops

Looping means repeating something over and over until a particular
condition is satisfied.

Python has two primitive loop commands:

-   `while` loops
-   `for` loops

### For loop

A `for` loop is used for iterating over a sequence.

``` python
for x in fruits:
    print(x)
```

### Range

``` python
for x in range(y):
    print(x)
```

### Nested loops

``` python
for x in adj:
    for y in fruits:
        print(x, y)
```

### Continue statement

``` python
for x in y:
    if x == "z":
        continue
```

### Break statement

``` python
for x in y:
    print(x)
    if x == "y":
        break
```

### While loop

In a `while` loop, a set of statements can be executed as long as a
condition is true.

``` python
i = 1

while i < 6:
    print(i)
    i += 1
```

### Break in a while loop

``` python
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

### Continue in a while loop

``` python
i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
```

## Functions

A function is a block of code that only runs when called.

You can pass data, known as parameters, into a function. A function can
return data as a result.

### Defining and calling a function

``` python
def function_name():
    # statements

function_name()
```

### Function topics

-   Arguments
-   Arbitrary arguments: `*args`
-   Arbitrary keyword arguments: `**kwargs`
-   Default parameter values
-   Return values

------------------------------------------------------------------------

*End of the Python Workshop presentation content.*
