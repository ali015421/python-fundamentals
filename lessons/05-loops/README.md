## 05-loops/README.md

### What this covers
for loops with range(), while loops with a condition, infinite loop risk.

### The problem
Needed to repeat an action a known number of times (print a sequence) and
an unknown number of times until a condition changes (model compound
interest growth year over year).

### Approach
Built two examples: a simple for i in range(5) counter, and a while loop
modeling 5 years of compound interest growth on a starting balance.

### Key concepts practiced
- range(n) generates n values, starting at 0, stopping before n
- while loops repeat as long as a condition stays True — and need something
  inside the loop that eventually makes the condition False, or it becomes
  an infinite loop
- Compound interest: multiplying the running balance by (1 + rate) each
  pass, not recalculating from the original principal each time

### Bugs I hit
- Initially wrote the interest formula as balance * (20 + rate) instead of
  balance * (1 + rate) while experimenting — produced an absurd, obviously
  wrong result, which made the correct formula's logic click harder.

### How to run
```
python3 lesson.py
```

### What I'd improve
Could parameterize the loop (number of years, starting balance) instead of
hardcoding them.

### Career connection
This is literally the mechanic behind any multi-year financial projection
or amortization schedule.
