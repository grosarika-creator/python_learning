# Session 7: Functions, Scope, and Recursion

- **Date**: 2026-09-21
- **Topic**: Functions, return values, variable scope, and recursive logic

## Overview

In this session, I moved from writing small procedural scripts to organizing my code into reusable functions. I learned how to define functions, call them, return values, and understand how variables can behave differently inside and outside a function. I also practiced a recursive function and a small IELTS helper program, which showed me how functions can make programs more structured and easier to maintain.

---

## Files and Explanations

### `[function.py](./function.py)`

- **Concept**: Defining functions and parameter handling
- **Explanation**:
  This file introduced me to functions as reusable blocks of code. I created simple functions such as `greeting()` and `greeting_with_tone()`, and I learned that functions can take input values and produce different results depending on those values. This was a major step forward because I started to see how code can be organized into smaller, clearer parts.
- **Possible Improvements**:
  - Add docstrings to explain what each function does.
  - Use more consistent naming for readability.
  - Try writing a function that returns a value instead of only printing.

---

### `[function_caller.py](./function_caller.py)`

- **Concept**: Calling functions from another file
- **Explanation**:
  This script showed me how functions can be imported and reused from another module. I learned that code can be split into multiple files, making the project more organized. This is an important concept because real-world programs often grow beyond a single file.
- **Possible Improvements**:
  - Add comments to explain the import process.
  - Use a package structure when the project becomes larger.
  - Practice calling functions with different arguments to see the behavior clearly.

---

### `[function_with_return.py](./function_with_return.py)`

- **Concept**: Functions returning values
- **Explanation**:
  In this file, I created a function that calculates the average of a list of scores and returns the result. This taught me the difference between printing from inside a function and returning a value for use elsewhere in the program. It also showed me that functions are much more useful when they can give back information instead of only displaying output.
- **Possible Improvements**:
  - Add input validation for empty score lists.
  - Use better variable names such as `score_list`.
  - Try a version that accepts user input directly.

---

### `[variable_scope.py](./variable_scope.py)`

- **Concept**: Variable scope and the `global` keyword
- **Explanation**:
  This script helped me understand that variables can have different scopes inside and outside functions. I saw that changes inside a function do not always affect the outer variable unless I explicitly declare them as global. This was an important concept because scope rules affect how data flows through a program.
- **Possible Improvements**:
  - Add a simple explanation of local versus global variables.
  - Avoid using `global` unless it is truly necessary.
  - Practice a version without `global` to see cleaner alternatives.

---

### `[recursion.py](./recursion.py)`

- **Concept**: Recursive functions
- **Explanation**:
  This file introduced me to recursion, where a function calls itself until it reaches a base case. I used a list of scores and summed them by calling the function on the remaining slice of the list. This was a big conceptual step because recursion is a different way to solve problems compared to loops.
- **Possible Improvements**:
  - Add comments explaining the base case and recursive step.
  - Try a recursion example with Fibonacci numbers or factorials.
  - Compare recursion and loops side by side to understand when each is useful.

---

### `[prime_number_function.py](./prime_number_function.py)`

- **Concept**: Reusing prime-checking logic in a function
- **Explanation**:
  In this script, I moved the prime-checking logic into a function and returned a boolean result. This made the code more reusable and easier to read. It also helped me see how functions can package logic into a single unit that I can call whenever I need it.
- **Possible Improvements**:
  - Add input validation for negative numbers.
  - Handle `0` and `1` with a clearer message.
  - Compare this function with the earlier loop-based version.

---

### `[ielts_progress_checker.py](./ielts_progress_checker.py)`

- **Concept**: Combining functions to build a real-world program
- **Explanation**:
  This file brought together many ideas from the lesson. I created functions for feedback, recommendations, and average calculation, and then used them to build a small IELTS progress checker. This was a strong example of how functions can help organize a larger program, making it easier to understand and extend.
- **Possible Improvements**:
  - Separate the logic into smaller helper functions for even cleaner code.
  - Add input validation for empty or invalid skill names.
  - Store results in a dictionary or list to make the program more expandable.

---

## Key Takeaways

- I learned that functions help organize code and reduce repetition.
- I understood the difference between code that prints output and code that returns values.
- I practiced variable scope and saw how functions can affect data flow.
- I introduced recursion and learned how to stop it with a base case.
- I saw how functions can turn a simple script into a more structured and useful program.
