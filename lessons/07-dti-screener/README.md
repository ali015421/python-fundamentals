## 07-dti-screener/README.md

### What this covers
input() with type conversion, a function-based real screening tool
combining earlier concepts (variables, operators, conditionals, functions).

### The problem
A bank-style tool: take a customer's monthly income and monthly debt
payments, calculate debt-to-income ratio, approve if DTI is under 40%,
otherwise reject.

### Approach
Took income and debt as user input, converted to numeric types, passed them
into a function that calculates and returns the DTI ratio, then used
if/else on the result to decide approve/reject and print the DTI as a
percentage.

### Key concepts practiced
- input() always returns a string — must wrap in int()/float() before doing
  math with it
- Designing a function to take parameters explicitly (income, debt) instead
  of silently relying on outer/global variables, so it's self-contained and
  reusable on its own

### Bugs I hit
- Missing colon after the def line (SyntaxError)
- Defined a parameter (debt_to_income) but never actually used it — the
  function was silently relying on outer variables instead, which is bad
  practice even if it happens to run
- Inconsistent indentation on the return line
- Initially had no approve/reject decision logic or output at all — just the
  calculation
All fixed by rewriting the function to properly take income and debt as
parameters, use them directly, and adding the if/else decision plus print
output after calling the function.

### How to run
```
python3 lesson.py
```
Enter monthly income and monthly debt payments when prompted.

### What I'd improve
No validation for negative numbers or zero income (would crash on
division by zero).

### Career connection
DTI screening is real SBP/bank-style loan eligibility logic — this is a
direct building block toward the planned Loan Eligibility Screener project.
