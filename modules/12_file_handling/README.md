# Module 12 -- File Handling and JSON

File handling lets a program save information and read it later.

## Write to a file

``` python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
```

`with` closes the file automatically when the block ends.

## File modes

-   `r`: read
-   `w`: write, replacing existing contents
-   `a`: append
-   `x`: create a new file and fail if it already exists

## Read a file

``` python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

## JSON

JSON stores structured data as text. Python's built-in `json` module can
write and read it.

``` python
import json

student = {"name": "Asha", "mark": 90}
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded["name"])
```

## Try it

Write three lines to a file, read them, then save and load a student's
details using JSON.
