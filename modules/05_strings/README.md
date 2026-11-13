# Module 05 -- Strings

A string is text written inside single, double or triple quotes.

``` python
name = "Python"
message = 'Hello'
multiline = """This is
a multi-line string."""
```

## Indexing and slicing

Python indexes start at zero. Negative indexes count from the end. A
slice's end position is not included.

``` python
word = "PYTHON"
print(word[0])    # P
print(word[-1])   # N
print(word[1:4])  # YTH
```

## Useful methods

``` python
text = "  Hello Python  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "World"))
print(len(text))
```

Strings are immutable: methods return a new string rather than changing
the original.

## Try it

Ask for a name and print it in uppercase. Display the first and last
characters of a word. Remove extra spaces from a sentence.
