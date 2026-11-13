# Module 06 -- Data Structures

Data structures store collections of values.

## Lists

Lists are ordered, changeable and allow duplicates.

``` python
fruits = ["apple", "banana", "apple"]
fruits.append("mango")
fruits[1] = "orange"
print(fruits)
```

Common methods include `append()`, `insert()`, `extend()`, `remove()`,
`pop()` and `sort()`.

## Tuples

Tuples are ordered but cannot be changed after creation.

``` python
location = (10.0, 76.3)
print(location[0])
```

## Sets

Sets store unique values and do not support positional indexing.

``` python
numbers = {1, 2, 2, 3}
numbers.add(4)
print(numbers)
```

## Dictionaries

Dictionaries store key-value pairs.

``` python
student = {"name": "Asha", "mark": 92}
print(student["name"])
student["mark"] = 95
student["city"] = "Kochi"
```

Useful methods: `keys()`, `values()`, `items()`, `get()`, `update()` and
`pop()`.

## Try it

Create a list of five foods, a tuple containing a location, a set of
unique numbers and a dictionary describing a student.
