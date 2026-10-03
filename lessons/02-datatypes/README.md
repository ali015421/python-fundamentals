## 02-datatypes/README.md

### What this covers
Core data types: int, float, str, bool, and how type() reveals them.

### The problem
Needed to understand what kind of value a variable holds, since different
types behave differently in math and comparisons.

### Approach
Ran type() checks directly in the terminal to see real output instead of
guessing from the concept.

### Key concepts practiced
- int, float, str, bool and their type() output format (<class 'int'>)
- bool is technically a subclass of int, but kept separate for readability —
  a logical result should look different from a quantity in code

### Bugs I hit
- Tried running type() calls without print() in a script file — nothing
  displayed, since that only auto-prints in an interactive shell, not a
  saved .py file.

### How to run
```
python3 lesson.py
```

### What I'd improve
N/A — foundational lesson.

### Career connection
Distinguishing numeric vs boolean columns matters constantly in pandas
later — same concept, different syntax.
