## 06-functions/README.md

### What this covers
Defining functions with def, parameters, return values, calling with
different arguments.

### The problem
Had repeated calculation logic (discount math, simple formulas) that needed
to work on different input values without rewriting the same lines each time.

### Approach
Built two small functions (add_ten, apply_discount) to isolate the core
mechanic — parameter in, calculation, return — before applying it to a real
business case.

### Key concepts practiced
- Parameters are placeholders that only exist inside the function, filled in
  per call
- return hands a value back for reuse, unlike print() which only displays it
  and gives nothing back to the program
- Same function, different arguments, zero duplicated code

### Bugs I hit
- Mismatched indentation — wrote result = number + 10 with no indentation
  under def add_ten(number):, while return result was indented. Caused an
  IndentationError. Fixed by making sure every line inside a function body
  has consistent indentation.

### How to run
```
python3 lesson.py
```

### What I'd improve
Could add input validation (e.g. reject negative numbers).

### Career connection
Functions are literally what a reusable financial formula (ratio
calculation, tax calculation) becomes in code — build once, call on any
dataset.
