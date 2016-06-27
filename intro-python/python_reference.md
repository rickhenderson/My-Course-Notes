# CP104 Python Reference

## List of functions

### Introduction: CP102 Week 1
* print
* input


### Formatted Output: CP102 Week 2
* `print("Values: {}".format())`
* Formatting code: {:[[fill]align][sign][width][,][.precision][type]}
* mixed formatting example:

```Python
# Mixed Formatting
> print("|{:>9d}| |{:>9.2f}| |{:>15s}|".format(integer, decimal, phrase))
|    12345| |   123.45| |       Hi there|
```
* Common: `{.2f}` for displaying 2 decmial places

### Decisions: CP104 Week 3
* `if...elif...else`

### Repetition: While - CP104 Week 4
* `from random import randint, randrange, random, uniform`
* randint
* randrange
* random
* uniform

### Repetition: For - CP104 Week 5
* for
* advanced print
   * `print(" {}".format(i), end = "")`

### Math Methods - CP104 Week 6
`from math import ...`
* cos
* sin
* degrees
* radians
* acos
* asin

### String Methods - CP104 Week 7

* Subsetting / Segmenting: _string_[_start_:_end_]
* upper
* lower
* swapcase
* capitalize
* title
* isalnum
* isalpha
* isdigit
* isspace
* isupper
* islower
* split(_delimiter_)
* lstrip
* rstrip
* strip
* count(_srch_)
* find(_srch_)
* rfind(_srch_)
* startswith(_prefix_)
* endswith(_prefix_)
* `print("a" in name) # Returns True`
* 'A' comes before 'a' in the ASCII table

### Lists - CP104 Week 8

* lists are **mutable**
* list segmenting or *slicing*
* pop(), pop(i)
* append
* reverse
* extend
* insert(i, value)
* del x[0]

### Files - CP104 Week 9

* Files are treated as objects
* `file_variable = open(file_name, mode, encoding="utf-8")`
  * utf-8 is a good default for standard ASCII and a few non-English characters
* different modes for reading, writing, and appending
  * also modes for r+, w+, a+
* `first_file.close()`
* try and only open a file once if possible, close when done
* `first_file.readline()` reads in the line and the terminator
* reading a file and stripping the EOL characters:

```Python
first_file = open("data.txt", "r", encoding="utf-8")
line = first_file.readline().strip()

while line != "":
    # process data
    line = first_file.readline().strip()
```


### 2D Lists - CP104 Week 10
