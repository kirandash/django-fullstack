# Python

## 1. Intro and Setup
### 1.1 Topics to cover
1. **Basics**
    - Numbers, Strings, Lists, Dictionaries
    - Tuples, Sets, Booleans
    - Control Flow
    - Functions
2. **Advanced**
    - Scope
    - Object Oriented Programming
    - Errors and Exceptions
    - Decorators
    - Regular Expressions

### 1.2 Explore 3 ways to Install Python
1. Only Python: https://www.python.org/downloads/
2. Python distribution: A distribution is a version of Python that also comes pre-packaged with additional useful libraries
3. Distributions:
    - **Anaconda**: https://www.anaconda.com/products/individual
    - **Miniconda**: https://docs.conda.io/en/latest/miniconda.html : a smaller version of Anaconda without the additional packages
4. check version of installed python: `python --version` will return 2.7.16
    - `python3 --version`: will return 3.8.3
5. For Linting and debugging: Add Python extension by Microsoft in VSCode

## 2. Basic Python Concepts
### 2.1 Numbers
1. Numbers in Python have two main forms:
    - Integer: Integers are whole numbers ex: 45
    - Floating Point Numbers: FPNs have a decimal in them ex: 45.8
2. Add code to basics/01_numbers.py file
2. **Steps to run python File**:
    - `cd python/basics/`
    - `python3 01_numbers.py`: Note: mac has both python 2 and 3 installed. Thus, mentioning explicitly to use python3.
    
### 2.2 Strings
1. Strings in Python are used to hold text information and are indicated with the use of single or double quotes.
2. basics/02_strings.py

### 2.3 Lists
1. Lists are Python's version of Arrays.
2. They behave similarly to JS Array.
3. Run: 
    - `cd python/basics/`
    - `python3 03_lists.py`

### 2.4 Dictionaries
1. Dictionaries are Python's version of Hash tables (Objects in JS)
2. Dictionaries allows us to create a mapping with key value pair.
3. Dictionaries doesn't retain any order.
4. Run:
    - `python3 04_dictionaries.py`

### 2.5 Tuples, Sets and Booleans
1. Tuples are immutable sequences
2. Sets are unordered collections of unique elements.
3. Booleans are just True / False statements
