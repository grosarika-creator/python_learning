# Session 6: Loop Control Flow & Conditional Expressions

- **Date**: 2026-09-18
- **Topic**: `continue`, `break`, `else` with loops, and compact conditional logic

## Overview

In this lesson, I learned how to control the flow of loops more precisely. I explored the use of `continue` and `break`, practiced `for...else` and `while...else` patterns, and saw how conditional expressions can shorten simple `if` statements. This helped me understand that Python can write code in both long and compact forms, and that the cleaner version is often easier to read once you understand the idea.

---

## Files and Explanations

### `[control_flow.py](./control_flow.py)`

- **Concept**: Controlling loop flow with `break` and `continue`
- **Explanation**:
  This file showed me how to stop a loop early with `break` and skip certain iterations with `continue`. I used it to filter even and odd numbers by controlling which iterations should be printed. This was an important lesson because loops are not only about repetition; they are also about deciding which parts of the repetition should happen.
- **Possible Improvements**:
  - Add comments explaining why `continue` skips a value.
  - Separate the odd and even examples into clearer sections.
  - Try using a simpler input example to make the logic easier to grasp.

---

### `[for_else.py](./for_else.py)`

- **Concept**: `for...else` loop patterns
- **Explanation**:
  In this file, I learned that a `for` loop can have an `else` block that runs if no break occurs. This was a new pattern for me, and it helped me understand that Python provides concise ways to express “if no match was found.” I used it to check whether a list contained an odd number and print a message if it did not.
- **Possible Improvements**:
  - Add a short explanation of why the `else` block runs only when the loop finishes without breaking.
  - Try the same pattern with strings or dictionaries.
  - Keep the variable names more descriptive for beginner readers.

---

### `[while_else.py](./while_else.py)`

- **Concept**: `while...else` loop patterns
- **Explanation**:
  This script showed me the same idea as `for...else`, but with a `while` loop. I learned that if the loop completes without a break, the `else` block executes. This is useful in situations where I want to distinguish between “found a result” and “loop finished without success.”
- **Possible Improvements**:
  - Add comments to show the difference between the normal version and the shorter version.
  - Practice with a real-world example such as a password guess loop.
  - Use more descriptive names like `attempts` and `word_guess`.

---

### `[conditional_expression.py](./conditional_expression.py)`

- **Concept**: Ternary-style conditional expressions
- **Explanation**:
  This file introduced me to a shorter way of writing simple `if...else` statements. Instead of writing multiple lines, I could write `value = True if condition else False`. This taught me that Python supports compact decision syntax that is useful for quick assignments and clean code when the logic is simple.
- **Possible Improvements**:
  - Add more examples with numeric comparisons.
  - Explain when the compact expression is easier to read and when it is not.
  - Keep the examples simple so the syntax is easy to understand.

---

## Key Takeaways

- I learned that `continue` skips the rest of the loop body for one iteration.
- I understood that `break` stops the loop immediately when a condition is met.
- I practiced the `for...else` and `while...else` patterns.
- I saw how Python supports shorter conditional expressions for simple decisions.
- I gained confidence in writing loops that are both controlled and readable.
