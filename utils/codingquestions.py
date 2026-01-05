import random

HARD_QUESTIONS = [
    # --- PYTHON ---
    {
        "question": "What is the output of this code?\n```python\nprint(type(lambda: None))\n```",
        "options": ["a) <class 'function'>", "b) <class 'lambda'>", "c) <class 'NoneType'>"],
        "correct": "a",
        "explanation": "Lambdas are functions in Python."
    },
    {
        "question": "Which of these is NOT a valid way to create a set?",
        "options": ["a) {1, 2}", "b) set([1, 2])", "c) {}"],
        "correct": "c",
        "explanation": "`{}` creates an empty dictionary, not a set. Use `set()` for an empty set."
    },
    {
        "question": "What is the output?\n```python\na = [1, 2, 3]\nb = a\na += [4]\nprint(b)\n```",
        "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) Error"],
        "correct": "b",
        "explanation": "`+=` on lists modifies the list in-place, so `b` (which references the same object) sees the change."
    },
    {
        "question": "What does the `__init__` method do?",
        "options": ["a) Initializes a class", "b) Initializes an object (instance)", "c) Creates a new module"],
        "correct": "b"
    },
    {
        "question": "What is the result of `print(0.1 + 0.2 == 0.3)`?",
        "options": ["a) True", "b) False", "c) Error"],
        "correct": "b",
        "explanation": "Floating point precision issues make 0.1 + 0.2 slightly larger than 0.3."
    },
    {
        "question": "Which decorator is used to define a class method?",
        "options": ["a) @static", "b) @classmethod", "c) @method"],
        "correct": "b"
    },
    {
        "question": "What is the output of `print('a' < 'b')`?",
        "options": ["a) True", "b) False", "c) Error"],
        "correct": "a",
        "explanation": "Strings are compared lexicographically (ASCII value)."
    },
    {
        "question": "What keyword is used to handle exceptions?",
        "options": ["a) catch", "b) except", "c) handle"],
        "correct": "b"
    },
    {
        "question": "What is a generator in Python?",
        "options": ["a) A function that returns a list", "b) A function that yields values one by one", "c) A tool to generate code"],
        "correct": "b"
    },
    {
        "question": "What is the output?\n```python\nx = (1)\nprint(type(x))\n```",
        "options": ["a) <class 'tuple'>", "b) <class 'int'>", "c) <class 'list'>"],
        "correct": "b",
        "explanation": "A single element tuple requires a comma: `(1,)`."
    },
    # --- JAVASCRIPT ---
    {
        "question": "What is the output of `console.log(typeof NaN)`?",
        "options": ["a) 'number'", "b) 'NaN'", "c) 'undefined'"],
        "correct": "a",
        "explanation": "NaN stands for Not-a-Number, but its type is technically 'number'."
    },
    {
        "question": "What is the result of `[] + []`?",
        "options": ["a) []", "b) '' (Empty String)", "c) 0"],
        "correct": "b",
        "explanation": "Arrays are converted to strings and concatenated."
    },
    {
        "question": "Which keyword declares a block-scoped variable?",
        "options": ["a) var", "b) let", "c) def"],
        "correct": "b"
    },
    {
        "question": "What is the output of `console.log(0.1 + 0.2 === 0.3)`?",
        "options": ["a) true", "b) false", "c) undefined"],
        "correct": "b",
        "explanation": "Floating point arithmetic."
    },
    {
        "question": "How do you create a Promise?",
        "options": ["a) new Promise((resolve, reject) => ...)", "b) Promise.create()", "c) async function()"],
        "correct": "a"
    },
    {
        "question": "What does `===` check?",
        "options": ["a) Value only", "b) Value and Type", "c) Reference"],
        "correct": "b"
    },
    {
        "question": "What is the output?\n```javascript\nconsole.log('5' - 3)\n```",
        "options": ["a) 2", "b) '53'", "c) NaN"],
        "correct": "a",
        "explanation": "The `-` operator converts the string to a number."
    },
    {
        "question": "What is a closure?",
        "options": ["a) A function bundled with its lexical environment", "b) The end of a function", "c) A closed class"],
        "correct": "a"
    },
    {
        "question": "Which method removes the last element from an array?",
        "options": ["a) shift()", "b) pop()", "c) remove()"],
        "correct": "b"
    },
    {
        "question": "What is the output?\n```javascript\nconsole.log(1 + '1')\n```",
        "options": ["a) 2", "b) '11'", "c) NaN"],
        "correct": "b",
        "explanation": "The `+` operator with a string performs concatenation."
    },
    # --- JAVA ---
    {
        "question": "What is the size of an `int` in Java?",
        "options": ["a) 16 bit", "b) 32 bit", "c) 64 bit"],
        "correct": "b"
    },
    {
        "question": "Which keyword is used to inherit a class?",
        "options": ["a) implements", "b) extends", "c) inherits"],
        "correct": "b"
    },
    {
        "question": "What is the default value of a boolean variable?",
        "options": ["a) true", "b) false", "c) null"],
        "correct": "b"
    },
    {
        "question": "Which collection allows duplicate elements?",
        "options": ["a) Set", "b) List", "c) Map (Keys)"],
        "correct": "b"
    },
    {
        "question": "What is the entry point of a Java program?",
        "options": ["a) public static void main(String[] args)", "b) void main()", "c) public void start()"],
        "correct": "a"
    },
    {
        "question": "Is Java pass-by-reference or pass-by-value?",
        "options": ["a) Pass-by-reference", "b) Pass-by-value", "c) Both"],
        "correct": "b",
        "explanation": "Java is strictly pass-by-value. Object references are passed by value."
    },
    {
        "question": "Which keyword makes a variable constant?",
        "options": ["a) const", "b) final", "c) static"],
        "correct": "b"
    },
    {
        "question": "What is the parent class of all classes in Java?",
        "options": ["a) Class", "b) Object", "c) Main"],
        "correct": "b"
    },
    {
        "question": "How do you compare two strings for equality?",
        "options": ["a) ==", "b) .equals()", "c) .compare()"],
        "correct": "b",
        "explanation": "`==` compares references, `.equals()` compares content."
    },
    {
        "question": "What is an interface?",
        "options": ["a) A class with only abstract methods (mostly)", "b) A concrete class", "c) A variable type"],
        "correct": "a"
    },
    # --- C++ ---
    {
        "question": "What is the output?\n```cpp\nint x = 5;\ncout << x++ << ++x;\n```",
        "options": ["a) 57", "b) 66", "c) Undefined Behavior"],
        "correct": "c",
        "explanation": "The order of evaluation of operands in `<<` is unspecified/undefined in older standards (before C++17)."
    },
    {
        "question": "Which operator is used to access members of a pointer?",
        "options": ["a) .", "b) ->", "c) ::"],
        "correct": "b"
    },
    {
        "question": "What is a destructor?",
        "options": ["a) A method to delete a class", "b) A method called when an object is destroyed", "c) A method to free memory manually"],
        "correct": "b"
    },
    {
        "question": "What is the difference between `struct` and `class`?",
        "options": ["a) No difference", "b) Default access specifier", "c) Structs cannot have methods"],
        "correct": "b",
        "explanation": "Struct members are public by default; class members are private."
    },
    {
        "question": "What does `virtual` keyword do?",
        "options": ["a) Enables polymorphism", "b) Makes a function faster", "c) Creates a virtual machine"],
        "correct": "a"
    },
    {
        "question": "How do you allocate memory dynamically?",
        "options": ["a) malloc", "b) new", "c) Both"],
        "correct": "c"
    },
    {
        "question": "What is a reference?",
        "options": ["a) A pointer", "b) An alias for an existing variable", "c) A copy of a variable"],
        "correct": "b"
    },
    {
        "question": "What is the STL?",
        "options": ["a) Standard Template Library", "b) Standard Type List", "c) Simple Text Language"],
        "correct": "a"
    },
    {
        "question": "What is `std::vector`?",
        "options": ["a) A static array", "b) A dynamic array", "c) A linked list"],
        "correct": "b"
    },
    {
        "question": "What is the size of an empty class?",
        "options": ["a) 0 bytes", "b) 1 byte", "c) 4 bytes"],
        "correct": "b",
        "explanation": "To ensure that two different objects have different addresses."
    },
    # --- C# ---
    {
        "question": "Which keyword is used for inheritance?",
        "options": ["a) extends", "b) :", "c) implements"],
        "correct": "b"
    },
    {
        "question": "What is LINQ?",
        "options": ["a) Language Integrated Query", "b) Linked Integer Queue", "c) List Index Query"],
        "correct": "a"
    },
    {
        "question": "What is the base class for all types in C#?",
        "options": ["a) System.Object", "b) System.Base", "c) System.Root"],
        "correct": "a"
    },
    {
        "question": "Which keyword is used to define an asynchronous method?",
        "options": ["a) await", "b) async", "c) thread"],
        "correct": "b"
    },
    {
        "question": "What is a nullable type?",
        "options": ["a) int?", "b) int!", "c) null<int>"],
        "correct": "a"
    },
    {
        "question": "What is the difference between `ref` and `out`?",
        "options": ["a) `out` requires initialization before passing", "b) `ref` requires initialization before passing", "c) No difference"],
        "correct": "b"
    },
    {
        "question": "What is a property?",
        "options": ["a) A variable", "b) A member that provides a flexible mechanism to read, write, or compute the value of a private field", "c) A method"],
        "correct": "b"
    },
    {
        "question": "What does `using` statement do?",
        "options": ["a) Imports a namespace", "b) Ensures IDisposable objects are disposed", "c) Both"],
        "correct": "c"
    },
    # --- RUST ---
    {
        "question": "What is the ownership model?",
        "options": ["a) A way to manage memory without a garbage collector", "b) A way to buy code", "c) A licensing model"],
        "correct": "a"
    },
    {
        "question": "Which keyword defines a mutable variable?",
        "options": ["a) var", "b) let mut", "c) mut"],
        "correct": "b"
    },
    {
        "question": "What is `Option<T>`?",
        "options": ["a) A type that represents an optional value (Some or None)", "b) A configuration option", "c) A compiler flag"],
        "correct": "a"
    },
    {
        "question": "What is the output of `println!(\"{}\", 5)`?",
        "options": ["a) 5", "b) {5}", "c) Error"],
        "correct": "a"
    },
    {
        "question": "What is a `Result` type used for?",
        "options": ["a) Returning values", "b) Error handling", "c) Math calculations"],
        "correct": "b"
    },
    {
        "question": "What does `unwrap()` do?",
        "options": ["a) Extracts the value from Option/Result or panics", "b) Opens a file", "c) Decrypts data"],
        "correct": "a"
    },
    {
        "question": "What is a trait?",
        "options": ["a) A class", "b) A collection of methods that can be implemented by types", "c) A variable type"],
        "correct": "b"
    },
    {
        "question": "How do you create a new vector?",
        "options": ["a) Vector.new()", "b) vec![]", "c) list[]"],
        "correct": "b"
    },
    {
        "question": "What is the borrow checker?",
        "options": ["a) A library", "b) A compiler part that enforces ownership rules", "c) A linter"],
        "correct": "b"
    },
    {
        "question": "What is `match`?",
        "options": ["a) A regex tool", "b) A control flow operator for pattern matching", "c) A game"],
        "correct": "b"
    },
    # --- WEB DEV (HTML/CSS) ---
    {
        "question": "What does HTML stand for?",
        "options": ["a) Hyper Text Markup Language", "b) High Tech Modern Language", "c) Hyperlinks and Text Markup Language"],
        "correct": "a"
    },
    {
        "question": "Which tag is used for the largest heading?",
        "options": ["a) <head>", "b) <h6>", "c) <h1>"],
        "correct": "c"
    },
    {
        "question": "What does CSS stand for?",
        "options": ["a) Computer Style Sheets", "b) Cascading Style Sheets", "c) Creative Style Sheets"],
        "correct": "b"
    },
    {
        "question": "Which property changes text color?",
        "options": ["a) text-color", "b) color", "c) font-color"],
        "correct": "b"
    },
    {
        "question": "What is the Box Model?",
        "options": ["a) A layout concept (Content, Padding, Border, Margin)", "b) A 3D model", "c) A flexbox container"],
        "correct": "a"
    },
    {
        "question": "Which unit is relative to the font-size of the root element?",
        "options": ["a) em", "b) rem", "c) px"],
        "correct": "b"
    },
    {
        "question": "What is Flexbox?",
        "options": ["a) A layout module for one-dimensional layouts", "b) A grid system", "c) A JavaScript library"],
        "correct": "a"
    },
    {
        "question": "Which tag is used to link a JavaScript file?",
        "options": ["a) <link>", "b) <script>", "c) <js>"],
        "correct": "b"
    },
    {
        "question": "What does `z-index` control?",
        "options": ["a) Zoom level", "b) Stack order of elements", "c) Opacity"],
        "correct": "b"
    },
    {
        "question": "What is the difference between `id` and `class`?",
        "options": ["a) `id` is unique, `class` can be reused", "b) `class` is unique", "c) No difference"],
        "correct": "a"
    },
    # --- GAME DEV ---
    {
        "question": "What is a Game Loop?",
        "options": ["a) A loop that runs the game logic and rendering repeatedly", "b) A level that repeats", "c) A bug"],
        "correct": "a"
    },
    {
        "question": "What is a Sprite?",
        "options": ["a) A 3D model", "b) A 2D image or animation", "c) A sound effect"],
        "correct": "b"
    },
    {
        "question": "What is a Collider?",
        "options": ["a) A component that handles physics collisions", "b) A weapon", "c) A script"],
        "correct": "a"
    },
    {
        "question": "What engine uses C# as its primary scripting language?",
        "options": ["a) Unreal Engine", "b) Unity", "c) Godot"],
        "correct": "b"
    },
    {
        "question": "What is Raycasting?",
        "options": ["a) Casting a spell", "b) Projecting a line to detect objects", "c) Rendering shadows"],
        "correct": "b"
    },
    {
        "question": "What is FPS?",
        "options": ["a) First Person Shooter / Frames Per Second", "b) Fast Player Speed", "c) Frames Per Screen"],
        "correct": "a"
    },
    {
        "question": "What is a Mesh?",
        "options": ["a) A collection of vertices, edges, and faces defining a 3D shape", "b) A texture", "c) A network"],
        "correct": "a"
    },
    {
        "question": "What is Delta Time?",
        "options": ["a) The time difference between the current and previous frame", "b) The total game time", "c) A loading screen"],
        "correct": "a",
        "explanation": "Used to make movement frame-rate independent."
    },
    # --- PHP ---
    {
        "question": "What does PHP stand for?",
        "options": ["a) Personal Home Page", "b) PHP: Hypertext Preprocessor", "c) Private Hosting Platform"],
        "correct": "b"
    },
    {
        "question": "How do you start a PHP block?",
        "options": ["a) <php>", "b) <?php", "c) <script>"],
        "correct": "b"
    },
    {
        "question": "Which symbol starts a variable in PHP?",
        "options": ["a) @", "b) $", "c) %"],
        "correct": "b"
    },
    {
        "question": "How do you print text in PHP?",
        "options": ["a) echo", "b) print", "c) Both"],
        "correct": "c"
    },
    {
        "question": "Which superglobal holds form data sent via POST?",
        "options": ["a) $_GET", "b) $_POST", "c) $_REQUEST"],
        "correct": "b"
    },
    {
        "question": "How do you connect to a MySQL database?",
        "options": ["a) mysqli_connect()", "b) PDO", "c) Both"],
        "correct": "c"
    },
    # --- OTHER / GENERAL ---
    {
        "question": "What is Git?",
        "options": ["a) A programming language", "b) A version control system", "c) A database"],
        "correct": "b"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["a) Structured Query Language", "b) Simple Question Language", "c) System Query List"],
        "correct": "a"
    },
    {
        "question": "What is Docker?",
        "options": ["a) A shipping company", "b) A platform for developing, shipping, and running applications in containers", "c) A code editor"],
        "correct": "b"
    },
    {
        "question": "What is an API?",
        "options": ["a) Application Programming Interface", "b) Apple Pie Ingredients", "c) Automated Program Instruction"],
        "correct": "a"
    },
    {
        "question": "What is Big O Notation?",
        "options": ["a) A way to measure code complexity/performance", "b) A large letter O", "c) A sorting algorithm"],
        "correct": "a"
    },
    {
        "question": "What is HTTP?",
        "options": ["a) HyperText Transfer Protocol", "b) High Tech Transfer Protocol", "c) HyperText Transmission Path"],
        "correct": "a"
    },
    {
        "question": "What is JSON?",
        "options": ["a) JavaScript Object Notation", "b) Java Standard Object Name", "c) Just Some Object Notes"],
        "correct": "a"
    },
    {
        "question": "What is a Bug?",
        "options": ["a) An insect", "b) An error or flaw in software", "c) A feature"],
        "correct": "b"
    }
]

def get_random_question():
    """Returns a random question from the list."""
    return random.choice(HARD_QUESTIONS)
