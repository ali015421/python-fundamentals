## 08-expense-tracker/README.md

### What this covers
Lists — creation, indexing, sum(), len(), looping directly over values.

### The problem
A small business wants to track a week's worth of expenses — not one
number, but several — and get the total and average at the end.

### Approach
Stored the week's expenses as a list instead of separate variables per
expense, used built-in sum() and len() to calculate total and average
rather than manually looping and adding.

### Key concepts practiced
- Lists hold multiple values under one name, in order, accessed by index
  starting at 0
- sum() and len() as built-in shortcuts — no manual loop needed for a total
- for expense in expenses loops over actual values directly, unlike
  range(), which loops over a count

### Bugs I hit
- None — predicted total (5100) and average (1020.0) correctly before
  running, and the first run matched exactly.

### How to run
```
python3 main.py
```

### What I'd improve
Right now the list is hardcoded. A real version should take expense entries
from user input (a loop collecting input() values until the user says
they're done) instead of a fixed list.

### Career connection
This is the exact shape of a single column in a spreadsheet or DataFrame —
sum()/len() here are literally what SUM()/AVERAGE() do in Excel and what
.sum()/.mean() will do in pandas later.
