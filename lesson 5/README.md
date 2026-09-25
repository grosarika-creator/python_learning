# Session 5: Loops, Patterns, and Repetition

- **Date**: 2026-09-14
- **Topic**: Iteration, looping, pattern generation, and repeated checks

## Overview

In this session, I learned how to repeat tasks in Python using loops. I practiced both `for` loops and `while` loops, and I used them to solve problems like finding the maximum value, checking whether a number is prime, and drawing star patterns. This lesson made me realize that loops are one of the most powerful tools in Python because they save time and reduce repetition in code.

---

## Files and Explanations

### `[for_loop.py](./for_loop.py)`

- **Concept**: Basic `for` loop iteration
- **Explanation**:
  This file introduced me to the idea of repeating a block of code with a `for` loop. I used `range()` to iterate through values and print messages repeatedly. This was a simple but important start because it showed me how loops can automate repeated tasks without writing the same line many times.
- **Possible Improvements**:
  - Use a more meaningful example than repeated greeting text.
  - Add a comment explaining how `range()` works.
  - Practice a loop that uses variables in a more realistic way.

---

### `[while_loop.py](./while_loop.py)`

- **Concept**: `while` loop and repeated user guessing
- **Explanation**:
  This script taught me that a `while` loop continues as long as a condition remains true. The user keeps guessing until the correct value is entered, and then the loop stops. This is a clear example of how loops can be used to keep prompting the user until the desired condition is met.
- **Possible Improvements**:
  - Add a maximum number of attempts to avoid endless loops.
  - Use more descriptive variable names such as `secret_number` and `user_guess`.
  - Show the attempt count to make the game more engaging.

---

### `[list_max_number.py](./list_max_number.py)`

- **Concept**: Finding a maximum value from a list
- **Explanation**:
  Here, I used a loop to scan a list of numbers and compare each value with the current maximum. This taught me how loops are useful when working with collections of data. I also learned that storing the first value as a starting maximum is a common strategy in this type of task.
- **Possible Improvements**:
  - Add comments explaining the comparison logic step by step.
  - Try using Python’s built-in `max()` function to compare methods.
  - Explain the difference between list iteration and input-based loops.

---

### `[max_number.py](./max_number.py)`

- **Concept**: Repeated input and comparison
- **Explanation**:
  This script asked the user to keep entering numbers until they typed `x` to stop. I then compared each input to the current maximum and tracked the largest number. This was a good example of how loops and conditionals work together in interactive programs.
- **Possible Improvements**:
  - Add validation so invalid input does not crash the program.
  - Show the number of values entered.
  - Use a clearer result message at the end.

---

### `[prime_number_checker.py](./prime_number_checker.py)`

- **Concept**: Checking prime numbers using loops
- **Explanation**:
  In this file, I checked whether a number was prime by counting how many divisors it had. I used a loop to test every number from 1 to the target, and then I checked the count. This exercise helped me understand how loops can be used to test mathematical conditions systematically.
- **Possible Improvements**:
  - Use a more efficient approach by stopping the loop early.
  - Add edge-case handling for values below 2.
  - Explain why prime numbers are only divisible by 1 and themselves.

---

### `[simple_prime_checker.py](./simple_prime_checker.py)`

- **Concept**: Simpler prime-checking logic
- **Explanation**:
  This version of the prime check was shorter and more direct. It set a default assumption and then tested whether the number was divisible by any value from 2 up to the number minus one. If a divisor was found, the loop stopped early. This taught me how to write cleaner looping logic and how to use `break` to make the program more efficient.
- **Possible Improvements**:
  - Add a clear explanation of why the loop starts from 2.
  - Handle the number 1 and 0 more explicitly.
  - Compare this version with the earlier checker to see which is easier to read.

---

### `[star_triangle.py](./star_triangle.py)`

- **Concept**: Nested loops and pattern generation
- **Explanation**:
  This script used nested loops to print a triangle pattern made of stars. I learned that an outer loop controls the number of rows, while an inner loop prints the stars in each row. This made me understand how loops can work together to build patterns and how repetition can produce visual output.
- **Possible Improvements**:
  - Add comments that describe the row and column logic.
  - Try making different patterns such as inverted triangles or pyramids.
  - Keep the pattern code separate from the explanation for readability.

---

### `[ielts_score_tracker.py](./ielts_score_tracker.py)`

- **Concept**: Looping with score tracking
- **Explanation**:
  This script tracked multiple IELTS practice scores until the user entered `x`. I used a `while` loop to keep collecting scores, compare them to the highest score, and print simple feedback based on each result. This was a great example of how loops and conditionals can work together in a learning or monitoring system.
- **Possible Improvements**:
  - Save scores into a list for later review.
  - Add average-score calculation at the end.
  - Use functions to separate the input and feedback logic.

---

## Key Takeaways

- I learned the difference between `for` loops and `while` loops.
- I used loops to repeat work, compare values, and inspect lists.
- I saw how `break` can stop a loop when a condition is met.
- I practiced pattern generation with nested loops.
- I understood that loops are essential for solving repetitive and data-driven problems.
