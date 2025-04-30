# Fun-With-Functions
https://canvas.eee.uci.edu/courses/16697/assignments/316519


Here's a quick review of each function based on the assignment specs:

---

### ✅ `cylinderVolume(radius, height)`
- ✔ Correct use of `math.pi`, follows the formula.
- 💡 Could simplify by returning the expression directly:
  ```python
  return math.pi * radius ** 2 * height
  ```

---

### ✅ `formatNumber(number)`
- ✔ Works as expected using Python string formatting.
- ✅ Handles both integers and floats correctly (decimals retained).
- 💡 You could add `type(number)` check if further validation is ever required, but not needed per the assignment.

---

### ✅ `securePassword(password)`
- ✔ Meets all security criteria.
- ✅ Checks length, case, digit, and special character.
- 💡 The variable naming is good but can be simplified:
  ```python
  if (countU and countL and countN and countS):
  ```

---

### ✅ `middleValue(a, b, c)`
- ✔ Correct logic using sorting.
- ✅ Returns middle value as required.

---

### ✅ `isBinary(number)`
- ✔ Converts number to string and checks for only `0` or `1`.
- 💡 Slight optimization using `set()`:
  ```python
  return set(str(number)).issubset({'0', '1'})
  ```

---

### ✅ `scramble(phrase)`
- ✔ Follows keyboard mapping correctly.
- ✅ Includes wrap-around and space handling.
- 💡 Minor enhancement: use `.get()` to prevent KeyErrors if unexpected characters sneak in (not necessary if precondition holds).

---

### ✅ `removeChars(phrase, remove)`
- ✔ Uses `str.replace()` in a loop for each character in `remove`.
- ✅ Effective and simple.
- 💡 Could use a comprehension for large strings, but your solution is fine and readable.

---

### ✅ `isPalindrome(phrase)`
- ✔ Removes spaces and normalizes case.
- ✅ Compares with reversed string accurately.
- 💡 Variable `rvs` is fine, could also inline it to reduce lines:
  ```python
  return phrase2 == phrase2[::-1]
  ```

---

### ✅ Submission & Naming
- ✔ Functions are named and structured as requested.
- ⚠ Make sure your script is saved and zipped correctly using the format `Lab1_YOURID.py`.

---

Sure! Here's how you can explain the project using the **STAR** format (Situation, Task, Action, Result):

---

### **S – Situation**
In a Python programming course, I was assigned a lab project that required implementing several utility functions to demonstrate foundational skills in data manipulation, string formatting, validation, and algorithmic problem-solving.

---

### **T – Task**
The task was to create a Python script with a collection of well-defined functions that each solve a specific problem. These included mathematical calculations (e.g., volume of a cylinder), data formatting, password validation, string scrambling, binary checking, and palindrome detection. The code needed to be correct, efficient, and follow good programming practices.

---

### **A – Action**
I wrote a total of eight functions:
- `cylinderVolume`: calculated the volume of a cylinder using `math.pi`.
- `formatNumber`: formatted numbers with commas for readability.
- `securePassword`: validated password strength by checking length and the presence of uppercase, lowercase, numeric, and special characters.
- `middleValue`: returned the median of three input values.
- `isBinary`: verified if a number contained only binary digits.
- `scramble`: transformed a string using a custom keyboard key mapping.
- `removeChars`: removed specific characters from a given phrase.
- `isPalindrome`: checked if a string was a palindrome after cleaning and normalizing it.

I used Pythonic constructs like `str.replace()`, `sort()`, slicing, and dictionary lookups to make the code clean and efficient. I also ensured readability through clear naming conventions and appropriate comments.

---

### **R – Result**
The final program passed all functional tests and was submitted successfully. It demonstrated my ability to handle diverse programming tasks, from string manipulation to logic-based validations. The project improved my confidence in Python programming and reinforced best practices such as clean code structure, modular design, and efficient algorithm implementation.

---

