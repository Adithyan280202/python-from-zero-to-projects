# Module 17 -- Git, GitHub and Testing

## Git and GitHub

Git is a version-control tool that records file changes. GitHub hosts
Git repositories online and supports collaboration.

## Basic Git workflow

``` bash
git status
git add .
git commit -m "Add first lesson"
git push
```

-   `status`: inspect changes.
-   `add`: stage changes.
-   `commit`: record a local snapshot.
-   `push`: send commits to the remote repository.

## Clone a repository

``` bash
git clone https://github.com/username/repository.git
```

## Simple checks with assert

``` python
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0
print("Checks passed")
```

## Testing with unittest

``` python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

Save as `test_add.py`, then run `python -m unittest`.

## Try it

Create a Git repository for a small program, commit a change, and write
two tests for a calculator function.
