# Module 11 -- Modules, Packages and Virtual Environments

## Modules

A module is a Python file containing reusable code. Suppose
`calculator.py` contains:

``` python
def add(a, b):
    return a + b
```

Use it in another file:

``` python
import calculator
print(calculator.add(2, 3))
```

You can import selected names:

``` python
from math import sqrt
print(sqrt(25))
```

## Packages

A package groups related modules in a directory, helping organise larger
programs.

## Virtual environments

A virtual environment keeps a project's Python packages separate from
other projects.

``` bash
python -m venv .venv
```

Activate in Windows PowerShell:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Deactivate with:

``` bash
deactivate
```

## Try it

Import `random`, generate a random integer, create your own conversion
module, and create a virtual environment.
