
## 04-control-flow/README.md

### What this covers
if / elif / else branching, combining logical operators inside conditions.

### The problem
Needed code to make decisions — e.g. approve/reject a loan based on income
and credit score — not just compute a fixed formula.

### Approach
Built a loan-approval-style if/elif/else chain, combining and inside
conditions, and traced through which branch would fire for different inputs.

### Key concepts practiced
- Only one branch in an if/elif/else chain ever runs, even if multiple
  conditions would technically also be True
- Indentation is syntax in Python, not just style — it defines what's
  inside a block

### Bugs I hit
- Left a variable (income) indented inside an unrelated if block by mistake.
  It happened to still work because that if condition was True during
  testing, but if it had been False, the variable would never have been
  created and later code would've crashed with a NameError. Fixed by
  un-indenting it to the correct top-level scope. This was a real lesson in
  how a bug can silently "work" during testing and still be wrong.

### How to run
```
python3 lesson.py
```

### What I'd improve
Could add explicit comments marking which block each variable belongs to,
for readability.

### Career connection
This is the backbone of business rules — loan approval, expense flagging,
budget variance checks — all boil down to if/elif/else logic.
