import random

HARD_QUESTIONS = [
    # --- PYTHON (EASY/MODERATE) ---
    {
        "question": "What is the output of `print(2 ** 3 ** 2)` in Python?",
        "options": ["a) 64", "b) 512", "c) 12"],
        "correct": "b",
        "explanation": "Exponentiation is right-associative. 3**2 = 9, then 2**9 = 512."
    },
    {
        "question": "Which of these is NOT a valid variable name in Python?",
        "options": ["a) _my_var", "b) 2my_var", "c) my_var2"],
        "correct": "b",
        "explanation": "Variable names cannot start with a number."
    },
    {
        "question": "What does the `len()` function do?",
        "options": ["a) Returns the length of an object", "b) Returns the type of an object", "c) Converts to a list"],
        "correct": "a"
    },
    {
        "question": "What is the output of `print('hello' * 2)`?",
        "options": ["a) hello2", "b) hellohello", "c) Error"],
        "correct": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) define", "c) def"],
        "correct": "c"
    },
    {
        "question": "What data type is `{'a': 1, 'b': 2}`?",
        "options": ["a) List", "b) Set", "c) Dictionary"],
        "correct": "c"
    },
    {
        "question": "How do you start a single-line comment in Python?",
        "options": ["a) //", "b) #", "c) /*"],
        "correct": "b"
    },
    {
        "question": "What is the result of `10 // 3` in Python?",
        "options": ["a) 3.33", "b) 3", "c) 4"],
        "correct": "b",
        "explanation": "`//` is the floor division operator."
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["a) push()", "b) add()", "c) append()"],
        "correct": "c"
    },
    {
        "question": "What is the output of `bool([])`?",
        "options": ["a) True", "b) False", "c) Error"],
        "correct": "b",
        "explanation": "Empty lists are considered False in boolean context."
    },
    {
        "question": "What does `range(5)` generate?",
        "options": ["a) 1, 2, 3, 4, 5", "b) 0, 1, 2, 3, 4", "c) 0, 1, 2, 3, 4, 5"],
        "correct": "b"
    },
    {
        "question": "Which operator is used for string concatenation?",
        "options": ["a) .", "b) +", "c) &"],
        "correct": "b"
    },
    {
        "question": "What is the output?\n```python\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)\n```",
        "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) Error"],
        "correct": "b",
        "explanation": "Lists are mutable and `y = x` creates a reference, not a copy."
    },
    {
        "question": "How do you check if a key 'k' exists in dictionary `d`?",
        "options": ["a) d.has('k')", "b) 'k' in d", "c) d.contains('k')"],
        "correct": "b"
    },
    {
        "question": "What is the correct way to import a module named `math`?",
        "options": ["a) include math", "b) import math", "c) using math"],
        "correct": "b"
    },
    {
        "question": "What does `str(123)` return?",
        "options": ["a) 123", "b) '123'", "c) [1, 2, 3]"],
        "correct": "b"
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": ["a) Tuple", "b) String", "c) List"],
        "correct": "c"
    },
    {
        "question": "What is the output of `print(type(1/2))`?",
        "options": ["a) <class 'int'>", "b) <class 'float'>", "c) <class 'number'>"],
        "correct": "b",
        "explanation": "Division `/` always returns a float in Python 3."
    },
    {
        "question": "How do you create an empty set?",
        "options": ["a) {}", "b) set()", "c) []"],
        "correct": "b",
        "explanation": "`{}` creates an empty dictionary."
    },
    {
        "question": "What is the output of `print('Python'[1])`?",
        "options": ["a) P", "b) y", "c) h"],
        "correct": "b",
        "explanation": "String indexing starts at 0."
    },
    {
        "question": "Which function reads input from the user?",
        "options": ["a) scan()", "b) read()", "c) input()"],
        "correct": "c"
    },
    {
        "question": "What is the output of `print(3 * '7')`?",
        "options": ["a) 21", "b) 777", "c) Error"],
        "correct": "b"
    },
    {
        "question": "Which statement is used to stop a loop?",
        "options": ["a) stop", "b) exit", "c) break"],
        "correct": "c"
    },
    {
        "question": "What is the output?\n```python\ndef func(a, b=2):\n    return a * b\nprint(func(3))\n```",
        "options": ["a) 3", "b) 6", "c) Error"],
        "correct": "b"
    },
    {
        "question": "How do you raise an exception?",
        "options": ["a) throw", "b) raise", "c) error"],
        "correct": "b"
    },
    {
        "question": "What is `__name__` when a script is run directly?",
        "options": ["a) '__main__'", "b) The filename", "c) None"],
        "correct": "a"
    },
    {
        "question": "Which method removes whitespace from the beginning and end of a string?",
        "options": ["a) trim()", "b) strip()", "c) clean()"],
        "correct": "b"
    },
    {
        "question": "What is the output of `print(list(range(2, 5)))`?",
        "options": ["a) [2, 3, 4, 5]", "b) [2, 3, 4]", "c) [3, 4, 5]"],
        "correct": "b"
    },
    {
        "question": "What keyword is used for class inheritance?",
        "options": ["a) extends", "b) inherits", "c) (ParentClass)"],
        "correct": "c"
    },
    {
        "question": "What is the output of `print(10 % 3)`?",
        "options": ["a) 3", "b) 1", "c) 3.33"],
        "correct": "b",
        "explanation": "`%` is the modulus operator (remainder)."
    },

    # --- JAVASCRIPT (EASY/MODERATE) ---
    {
        "question": "Which keyword is used to declare a constant in JavaScript?",
        "options": ["a) var", "b) let", "c) const"],
        "correct": "c"
    },
    {
        "question": "What is the output of `console.log(typeof [])`?",
        "options": ["a) array", "b) object", "c) list"],
        "correct": "b",
        "explanation": "Arrays are objects in JavaScript."
    },
    {
        "question": "How do you write 'Hello World' in an alert box?",
        "options": ["a) msg('Hello World')", "b) alert('Hello World')", "c) alertBox('Hello World')"],
        "correct": "b"
    },
    {
        "question": "What is `NaN`?",
        "options": ["a) Not a Number", "b) Null and None", "c) New array Number"],
        "correct": "a"
    },
    {
        "question": "Which operator checks for both value and type equality?",
        "options": ["a) ==", "b) ===", "c) ="],
        "correct": "b"
    },
    {
        "question": "What is the output of `'5' + 3` in JavaScript?",
        "options": ["a) 8", "b) '53'", "c) Error"],
        "correct": "b",
        "explanation": "JavaScript performs string concatenation."
    },
    {
        "question": "Which method converts a JSON string to a JavaScript object?",
        "options": ["a) JSON.parse()", "b) JSON.stringify()", "c) JSON.toObject()"],
        "correct": "a"
    },
    {
        "question": "What is the correct way to write a function in JavaScript?",
        "options": ["a) function:myFunc()", "b) function myFunc()", "c) def myFunc()"],
        "correct": "b"
    },
    {
        "question": "How do you call a function named `myFunction`?",
        "options": ["a) call myFunction()", "b) myFunction()", "c) run myFunction()"],
        "correct": "b"
    },
    {
        "question": "Which event occurs when the user clicks on an HTML element?",
        "options": ["a) onchange", "b) onmouseclick", "c) onclick"],
        "correct": "c"
    },
    {
        "question": "What is the output of `Boolean(10 > 9)`?",
        "options": ["a) true", "b) false", "c) NaN"],
        "correct": "a"
    },
    {
        "question": "Which symbol is used for comments in JavaScript?",
        "options": ["a) #", "b) //", "c) <!--"],
        "correct": "b"
    },
    {
        "question": "What is the correct syntax for a `for` loop?",
        "options": ["a) for (i = 0; i <= 5)", "b) for (i = 0; i <= 5; i++)", "c) for i = 1 to 5"],
        "correct": "b"
    },
    {
        "question": "How do you find the number with the highest value of x and y?",
        "options": ["a) Math.max(x, y)", "b) Math.ceil(x, y)", "c) top(x, y)"],
        "correct": "a"
    },
    {
        "question": "Which operator is used to assign a value to a variable?",
        "options": ["a) *", "b) =", "c) -"],
        "correct": "b"
    },
    {
        "question": "What is the output of `console.log(2 + '2')`?",
        "options": ["a) 4", "b) '22'", "c) NaN"],
        "correct": "b"
    },
    {
        "question": "Which keyword refers to the object belonging to the current code?",
        "options": ["a) self", "b) object", "c) this"],
        "correct": "c"
    },
    {
        "question": "How do you declare a variable that cannot be reassigned?",
        "options": ["a) var", "b) let", "c) const"],
        "correct": "c"
    },
    {
        "question": "What is the output of `console.log(!!'false')`?",
        "options": ["a) true", "b) false", "c) Error"],
        "correct": "a",
        "explanation": "Non-empty strings are truthy."
    },
    {
        "question": "Which array method removes the last element?",
        "options": ["a) shift()", "b) pop()", "c) push()"],
        "correct": "b"
    },

    # --- GENERAL PROGRAMMING & DSA (EASY/MODERATE) ---
    {
        "question": "What does HTML stand for?",
        "options": ["a) Hyper Text Markup Language", "b) High Tech Modern Language", "c) Hyperlinks and Text Markup Language"],
        "correct": "a"
    },
    {
        "question": "Which data structure uses LIFO (Last In First Out)?",
        "options": ["a) Queue", "b) Stack", "c) Array"],
        "correct": "b"
    },
    {
        "question": "What is the time complexity of accessing an array element by index?",
        "options": ["a) O(n)", "b) O(1)", "c) O(log n)"],
        "correct": "b"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["a) Structured Question Language", "b) Structured Query Language", "c) Simple Query Language"],
        "correct": "b"
    },
    {
        "question": "Which protocol is used for secure web browsing?",
        "options": ["a) HTTP", "b) FTP", "c) HTTPS"],
        "correct": "c"
    },
    {
        "question": "What is a 'bug'?",
        "options": ["a) A feature", "b) An error in code", "c) A type of virus"],
        "correct": "b"
    },
    {
        "question": "What does API stand for?",
        "options": ["a) Application Programming Interface", "b) Advanced Programming Interface", "c) Automated Program Interaction"],
        "correct": "a"
    },
    {
        "question": "Which is a binary number?",
        "options": ["a) 10101", "b) 202", "c) 12A"],
        "correct": "a"
    },
    {
        "question": "What is the base of the hexadecimal system?",
        "options": ["a) 10", "b) 8", "c) 16"],
        "correct": "c"
    },
    {
        "question": "Which sorting algorithm has the best average case time complexity?",
        "options": ["a) Bubble Sort", "b) Merge Sort", "c) Selection Sort"],
        "correct": "b",
        "explanation": "Merge Sort is O(n log n), others are O(n^2)."
    },
    {
        "question": "What is a 'loop'?",
        "options": ["a) A mistake in code", "b) A sequence of instructions repeated", "c) A connection between computers"],
        "correct": "b"
    },
    {
        "question": "What does CSS stand for?",
        "options": ["a) Computer Style Sheets", "b) Cascading Style Sheets", "c) Creative Style Sheets"],
        "correct": "b"
    },
    {
        "question": "Which data structure is best for a FIFO (First In First Out) system?",
        "options": ["a) Stack", "b) Queue", "c) Tree"],
        "correct": "b"
    },
    {
        "question": "What is 'recursion'?",
        "options": ["a) A function calling itself", "b) A loop that never ends", "c) A database query"],
        "correct": "a"
    },
    {
        "question": "What is 1 byte equal to?",
        "options": ["a) 4 bits", "b) 8 bits", "c) 16 bits"],
        "correct": "b"
    },
    {
        "question": "Which is NOT an Operating System?",
        "options": ["a) Linux", "b) Windows", "c) Oracle"],
        "correct": "c"
    },
    {
        "question": "What is the purpose of a compiler?",
        "options": ["a) To execute code line by line", "b) To translate source code to machine code", "c) To debug code"],
        "correct": "b"
    },
    {
        "question": "What is 'Open Source'?",
        "options": ["a) Software with free source code", "b) Software that costs money", "c) Software without copyright"],
        "correct": "a"
    },
    {
        "question": "What does GUI stand for?",
        "options": ["a) Graphical User Interface", "b) General User Interaction", "c) Global User Interface"],
        "correct": "a"
    },
    {
        "question": "Which is a NoSQL database?",
        "options": ["a) MySQL", "b) PostgreSQL", "c) MongoDB"],
        "correct": "c"
    },
    {
        "question": "What is the main function of an IP address?",
        "options": ["a) To identify a device on a network", "b) To store website data", "c) To encrypt data"],
        "correct": "a"
    },
    {
        "question": "What is 'Cloud Computing'?",
        "options": ["a) Computing using weather data", "b) Delivering computing services over the internet", "c) Wireless networking"],
        "correct": "b"
    },
    {
        "question": "What is a 'Boolean'?",
        "options": ["a) A text string", "b) A number", "c) A true/false value"],
        "correct": "c"
    },
    {
        "question": "Which is a version control system?",
        "options": ["a) Git", "b) Node.js", "c) Docker"],
        "correct": "a"
    },
    {
        "question": "What does JSON stand for?",
        "options": ["a) JavaScript Object Notation", "b) Java Standard Object Network", "c) JavaScript Online Notation"],
        "correct": "a"
    },

    # --- HARD / CHALLENGING (MIXED) ---
    {
        "question": "What is the output of this Python code?\n```python\ndef f(x, l=[]):\n    l.append(x)\n    return l\nprint(f(1))\nprint(f(2))\n```",
        "options": ["a) [1] then [2]", "b) [1] then [1, 2]", "c) [1] then [1]"],
        "correct": "b",
        "explanation": "Default mutable arguments are evaluated only once at function definition."
    },
    {
        "question": "In C++, what is the 'Diamond Problem' related to?",
        "options": ["a) Pointer arithmetic", "b) Multiple inheritance", "c) Memory leaks"],
        "correct": "b"
    },
    {
        "question": "What is the time complexity of QuickSort in the worst case?",
        "options": ["a) O(n log n)", "b) O(n)", "c) O(n^2)"],
        "correct": "c",
        "explanation": "Worst case occurs when the pivot is the smallest or largest element."
    },
    {
        "question": "What is the output of `[] + []` in JavaScript?",
        "options": ["a) []", "b) '' (Empty String)", "c) 0"],
        "correct": "b",
        "explanation": "Arrays are converted to strings and concatenated."
    },
    {
        "question": "What does the Python `GIL` prevent?",
        "options": ["a) Memory leaks", "b) Multiple threads executing Python bytecodes at once", "c) Deadlocks"],
        "correct": "b"
    },
    {
        "question": "Which design pattern ensures a class has only one instance?",
        "options": ["a) Factory", "b) Singleton", "c) Observer"],
        "correct": "b"
    },
    {
        "question": "What is the result of `0.1 + 0.2 === 0.3` in JavaScript?",
        "options": ["a) true", "b) false", "c) Error"],
        "correct": "b",
        "explanation": "Floating point precision issues make it 0.30000000000000004."
    },
    {
        "question": "In Python, what is a 'metaclass'?",
        "options": ["a) A class that inherits from itself", "b) A class of a class", "c) A class with static methods"],
        "correct": "b"
    },
    {
        "question": "What is 'Currying' in functional programming?",
        "options": ["a) Mixing multiple functions", "b) Transforming a function with multiple arguments into a sequence of functions", "c) Recursive function calls"],
        "correct": "b"
    },
    {
        "question": "What is the output?\n```python\nx = 10\ndef foo():\n    print(x)\n    x = 20\nfoo()\n```",
        "options": ["a) 10", "b) 20", "c) UnboundLocalError"],
        "correct": "c",
        "explanation": "Python treats `x` as local because of the assignment, but it's accessed before assignment."
    },
    {
        "question": "What is the difference between `process` and `thread`?",
        "options": ["a) Threads share memory, processes do not", "b) Processes share memory, threads do not", "c) No difference"],
        "correct": "a"
    },
    {
        "question": "What is a 'Closure' in JavaScript?",
        "options": ["a) A function with no arguments", "b) A function bundled with its lexical environment", "c) A method to close a window"],
        "correct": "b"
    },
    {
        "question": "What is the output of `print(type(type(int)))` in Python?",
        "options": ["a) <class 'type'>", "b) <class 'int'>", "c) <class 'object'>"],
        "correct": "a"
    },
    {
        "question": "Which of these is NOT a SOLID principle?",
        "options": ["a) Single Responsibility", "b) Open/Closed", "c) Loop Invariant"],
        "correct": "c"
    },
    {
        "question": "What is the space complexity of a recursive Fibonacci function without memoization?",
        "options": ["a) O(1)", "b) O(n)", "c) O(2^n)"],
        "correct": "b",
        "explanation": "The stack depth is n."
    },
    {
        "question": "What is 'Deadlock'?",
        "options": ["a) When a process terminates unexpectedly", "b) When two processes wait for each other indefinitely", "c) A memory error"],
        "correct": "b"
    },
    {
        "question": "What is the output of `print(all([]))` in Python?",
        "options": ["a) True", "b) False", "c) Error"],
        "correct": "a",
        "explanation": "Vacuous truth: all elements in the empty set are true."
    },
    {
        "question": "What is 'Polymorphism'?",
        "options": ["a) Hiding data", "b) Ability of different classes to be treated as instances of the same class", "c) Creating multiple copies of an object"],
        "correct": "b"
    },
    {
        "question": "What is the output of `print(any([]))` in Python?",
        "options": ["a) True", "b) False", "c) Error"],
        "correct": "b"
    },
    {
        "question": "In SQL, what is a 'Foreign Key'?",
        "options": ["a) A key used for encryption", "b) A field that links to the primary key of another table", "c) A unique identifier"],
        "correct": "b"
    },
    {
        "question": "What is the purpose of `__slots__` in Python?",
        "options": ["a) To reserve memory", "b) To restrict attribute creation and save memory", "c) To define private methods"],
        "correct": "b"
    },
    {
        "question": "What is the output of `console.log(1 < 2 < 3)` in JS?",
        "options": ["a) true", "b) false", "c) Error"],
        "correct": "a"
    },
    {
        "question": "What is the output of `console.log(3 > 2 > 1)` in JS?",
        "options": ["a) true", "b) false", "c) Error"],
        "correct": "b",
        "explanation": "3 > 2 is true (1). 1 > 1 is false."
    }
]

def get_random_question():
    """Get a random question from the pool"""
    return random.choice(HARD_QUESTIONS)

def get_questions_by_category(category: str, count: int = 5):
    """Get random questions from a specific category (future enhancement)"""
    # TODO: Implement category-based filtering
    return random.sample(HARD_QUESTIONS, min(count, len(HARD_QUESTIONS)))

def get_question_count():
    """Get total number of questions available"""
    return len(HARD_QUESTIONS)
