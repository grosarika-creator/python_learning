# Session 4: Conditionals & Decision Making

- **Date**: 2026-09-11
- **Topic**: If statements, comparisons, grading logic, and conditional checks

## Overview

In this session, I learned how to make decisions in Python using conditionals. I practiced comparing values, checking text patterns, and building logic flows for different conditions. I also created a few mini-applications such as score grading and sentence classification, which helped me understand how real decision-making programs work.

---

## Files and Explanations

### `[simple_condition.py](./simple_condition.py)`

- **Concept**: Basic `if` and `else` decisions
- **Explanation**:
  This script introduced me to the concept of checking a condition and then choosing a path based on the result. I used the sentence content to decide whether a phrase matched a condition and printed a message accordingly. This was my first step toward understanding that programs can react differently depending on input.
- **Possible Improvements**:
  - Use clearer variable names for better readability.
  - Add a few more examples with different conditions.
  - Write more beginner-friendly output messages.

---

### `[simple_condition2.py](./simple_condition2.py)`

- **Concept**: Grading logic with multiple conditions
- **Explanation**:
  In this file, I built logic for score ranges such as D, C, B, and A. I learned that the order of conditions matters a lot, especially when using comparisons like `<` and `<=`. This exercise helped me understand the importance of writing conditions in the right order so the program reaches the correct branch.
- **Possible Improvements**:
  - Add comments explaining the score ranges more clearly.
  - Refactor the condition sequence to be easier to follow.
  - Add input validation to reject invalid score values.

---

### `[simple_condition3.py](./simple_condition3.py)`

- **Concept**: `match` statements and alternate condition syntax
- **Explanation**:
  This script showed me a cleaner alternative to long `if` and `elif` chains using `match`. I learned how `match` can compare a value against several cases and fall back to a default case. It was a good introduction to more readable decision-making syntax in Python.
- **Possible Improvements**:
  - Add more sample cases to show clearer comparisons.
  - Use descriptive variable names like `customer_tier` instead of `tier`.
  - Explain how `match` differs from `if` for beginners.

---

### `[sentence_check.py](./sentence_check.py)`

- **Concept**: Sentence type detection
- **Explanation**:
  In this script, I checked whether a sentence ended with `?`, `!`, or `.` and then classified it as interrogative, imperative, or declarative. This taught me how Python can inspect text and make decisions based on patterns. It was a practical example of using string methods and conditionals together.
- **Possible Improvements**:
  - Add input trimming so spaces do not affect the result.
  - Handle uppercase or lowercase punctuation more carefully.
  - Extend the logic to classify more sentence types.

---

### `[max_number_simple.py](./max_number_simple.py)`

- **Concept**: Finding the maximum value
- **Explanation**:
  This file taught me how to compare three numbers and keep track of the biggest one. I learned that a starting value can be used as a reference, and then each number can be compared against it. This method helped me understand how a program can track a running maximum while checking several values.
- **Possible Improvements**:
  - Use a cleaner method to compare all numbers in one pass.
  - Add input validation for non-numeric values.
  - Explain why the starting value is important when comparing numbers.

---

### `[max_number.py](./max_number.py)`

- **Concept**: Nested conditionals for comparison
- **Explanation**:
  This version was more structured and showed me how nested `if` statements work. I compared the numbers in layers to determine which one was the largest. It made me realize that while nested conditions can be correct, they can also become harder to read if overused.
- **Possible Improvements**:
  - Use a simpler comparison method when possible.
  - Add comments to explain the decision tree.
  - Refactor the logic into a more readable pattern.

---

### `[ielts_band_checker.py](./ielts_band_checker.py)`

- **Concept**: Real-world decision logic with a user profile
- **Explanation**:
  This was one of the most practical exercises in the lesson. I created a simple IELTS band checker that accepted a student’s overall score and weakest skill, then returned a feedback message. I also used `match` to recommend practice based on the weakest skill. This helped me connect conditionals to real-world use cases.
- **Possible Improvements**:
  - Add validation for invalid band scores and skill names.
  - Use a cleaner output layout for easier reading.
  - Consider turning repeated logic into functions as the program grows.

---

## Key Takeaways

- I learned that `if`, `elif`, and `else` help programs make decisions.
- I discovered that the order of conditions matters in Python.
- I practiced comparing values and choosing different outputs based on those comparisons.
- I saw how `match` can make decision logic cleaner in some situations.
- I connected conditionals to practical examples like grading and feedback systems.
