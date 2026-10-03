
## 03-expressions-operators/README.md

### What this covers
Arithmetic, comparison, logical, and compound assignment operators.

### The problem
Needed to actually compute and compare values, not just store them —
calculating tax-style percentages, checking budget thresholds.

### Approach
Worked through each operator category with predict-before-run checks using
finance-style numbers (budget vs expenses, loan approval conditions).

### Key concepts practiced
- / always returns float, // floors down, % gives remainder, ** is exponent
- Comparison operators (>, <, ==, etc.) always return bool
- and requires both sides True, or requires at least one, not flips it
- Compound assignment (+=, -=, *=, /=) as shorthand for self-updating a variable

### Bugs I hit
- None major — mostly got operator precedence intuition solid here, which
  directly prevented a bigger bug later in the tax calculator project.

### How to run
```
python3 lesson.py
```

### What I'd improve
N/A — foundational lesson.

### Career connection
These are the exact operators behind pandas boolean masks and SQL WHERE
clauses later — same logic, applied across whole columns/tables at once.

