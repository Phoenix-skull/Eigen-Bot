import random

HARD_QUESTIONS = [
    # Python Questions (1-20)
    {"question": "What is the output of this Python code?\n`print([i for i in range(3)] is [0, 1, 2])`",
     "options": ["a) False", "b) True", "c) SyntaxError"], "correct": "a",
     "explanation": "`is` checks identity, not equality. Two separate list objects are never identical."},
    {"question": "Which Python built-in function is used to evaluate a string as a Python expression?",
     "options": ["a) compile()", "b) eval()", "c) exec()"], "correct": "b",
     "explanation": "eval() evaluates expressions, exec() executes statements, compile() creates code objects."},
    {"question": "What is the output of `type(lambda x: x)` in Python?",
     "options": ["a) <class 'function'>", "b) lambda", "c) function"], "correct": "a"},
    {"question": "Which algorithm is used in Python’s built-in `sort()` for lists?",
     "options": ["a) MergeSort", "b) TimSort", "c) QuickSort"], "correct": "b"},
    {"question": "What does GIL stand for in CPython?",
     "options": ["a) Garbage Integration Layer", "b) Global Interpreter Lock", "c) General Inline Logic"], "correct": "b"},
    {"question": "Which Python module allows low-level thread control?",
     "options": ["a) multiprocessing", "b) threading", "c) _thread"], "correct": "c"},
    {"question": "What does the Python `@staticmethod` decorator do?",
     "options": ["a) Create method without self", "b) Access instance variables", "c) Create class method"], "correct": "a"},
    {"question": "What is the output of this Python expression?\n`0.1 + 0.2 == 0.3`",
     "options": ["a) Error", "b) False", "c) True"], "correct": "b",
     "explanation": "Due to floating-point precision limitations, 0.1 + 0.2 equals approximately 0.30000000000000004"},
    {"question": "What happens if you don't close a file in Python?",
     "options": ["a) Nothing", "b) Data loss possible", "c) File deleted"], "correct": "b"},
    {"question": "How do you correctly handle potential exceptions in Python?",
     "options": ["a) try-finally", "b) try-except", "c) try-catch"], "correct": "b"},
    {"question": "What is a Python generator?",
     "options": ["a) A class for creating objects", "b) A function that returns an iterator", "c) A function that generates random numbers"], "correct": "b"},
    {"question": "What is the purpose of `__init__` method in Python classes?",
     "options": ["a) To define class methods", "b) To initialize object attributes", "c) To initialize a module"], "correct": "b"},
    {"question": "Which data type is immutable in Python?",
     "options": ["a) tuple", "b) dict", "c) list"], "correct": "a"},
    {"question": "What is list comprehension in Python?",
     "options": ["a) A method to sort lists", "b) A way to iterate over lists", "c) A concise way to create lists"], "correct": "c"},
    {"question": "What is a 'decorator' in Python?",
     "options": ["a) A type of class inheritance", "b) A design pattern for UI elements", "c) A function that modifies another function"], "correct": "c"},
    {"question": "Which built-in Python module is used for regular expressions?",
     "options": ["a) regex", "b) re", "c) regexp"], "correct": "b"},
    {"question": "What is a virtual environment in Python?",
     "options": ["a) An isolated environment for Python projects", "b) A cloud computing service", "c) A simulated operating system"], "correct": "a"},
    {"question": "What does `pip` stand for in Python?",
     "options": ["a) Python Installation Program", "b) Package Installer for Python", "c) Preferred Installer Program"], "correct": "c"},
    {"question": "How do you add an element to a Python set?",
     "options": ["a) .insert()", "b) .append()", "c) .add()"], "correct": "c"},
    {"question": "What is the difference between `==` and `is` in Python?",
     "options": ["a) `==` checks value, `is` checks identity", "b) They are interchangeable", "c) `==` checks identity, `is` checks value"], "correct": "a"},

    # Data Structures & Algorithms Questions (21-40)
    {"question": "Which of the following is a stable sorting algorithm?",
     "options": ["a) QuickSort", "b) HeapSort", "c) MergeSort"], "correct": "c"},
    {"question": "What is the average-case time complexity of Hash Table operations?",
     "options": ["a) O(n)", "b) O(1)", "c) O(log n)"], "correct": "b"},
    {"question": "Which data structure is used for implementing recursion internally?",
     "options": ["a) Queue", "b) Stack", "c) Heap"], "correct": "b"},
    {"question": "What’s the worst-case time complexity of QuickSort?",
     "options": ["a) O(n^2)", "b) O(n log n)", "c) O(log n)"], "correct": "a"},
    {"question": "What is tail recursion?",
     "options": ["a) Recursive calls with no base case", "b) A recursive call as the final action", "c) Recursion that returns a list"], "correct": "b"},
    {"question": "Which data structure allows access to elements only from one end (LIFO)?",
     "options": ["a) Linked List", "b) Queue", "c) Stack"], "correct": "c"},
    {"question": "What is the time complexity to search an element in a sorted array using Binary Search?",
     "options": ["a) O(1)", "b) O(log n)", "c) O(n)"], "correct": "b"},
    {"question": "Which of these is not a type of tree traversal?",
     "options": ["a) Midorder", "b) Inorder", "c) Postorder"], "correct": "a"},
    {"question": "What is a 'graph' in data structures?",
     "options": ["a) A hierarchical data structure", "b) A collection of nodes and edges", "c) A linear data structure"], "correct": "b"},
    {"question": "What is the primary characteristic of a 'Queue' data structure?",
     "options": ["a) Random access", "b) First-In, First-Out (FIFO)", "c) Last-In, First-Out (LIFO)"], "correct": "b"},
    {"question": "Which algorithm is best for finding the shortest path in an unweighted graph?",
     "options": ["a) Depth-First Search (DFS)", "b) Dijkstra's Algorithm", "c) Breadth-First Search (BFS)"], "correct": "c"},
    {"question": "What is a 'hash collision'?",
     "options": ["a) A sorting error", "b) When two keys hash to the same index", "c) A network error"], "correct": "b"},
    {"question": "What does 'Big O notation' describe?",
     "options": ["a) The best-case space complexity", "b) The worst-case time complexity of an algorithm", "c) The exact running time of an algorithm"], "correct": "b"},
    {"question": "Which sorting algorithm has the best worst-case time complexity?",
     "options": ["a) Bubble Sort", "b) Quick Sort", "c) Merge Sort"], "correct": "c"},
    {"question": "What is the primary advantage of a 'balanced binary search tree'?",
     "options": ["a) Simpler implementation", "b) Faster insertion only", "c) Guaranteed O(log n) search time"], "correct": "c"},
    {"question": "What is dynamic programming primarily used for?",
     "options": ["a) Managing memory dynamically", "b) Solving problems by breaking them into smaller subproblems and storing results", "c) Creating interactive user interfaces"], "correct": "b"},
    {"question": "What is a 'doubly linked list'?",
     "options": ["a) A list with two head pointers", "b) A list where each node has two values", "c) A list where each node points to the next and previous node"], "correct": "c"},
    {"question": "What is the purpose of 'memoization' in algorithms?",
     "options": ["a) To record function calls for debugging", "b) To optimize memory usage", "c) To store results of expensive function calls and return the cached result"], "correct": "c"},
    {"question": "Which search algorithm is generally faster on unsorted data?",
     "options": ["a) Binary Search", "b) Depth-First Search", "c) Linear Search"], "correct": "c"},
    {"question": "What is the difference between a 'stack' and a 'queue'?",
     "options": ["a) They are the same, just different names", "b) Stacks are FIFO, Queues are LIFO", "c) Stacks are LIFO, Queues are FIFO"], "correct": "c"},

    # C/C++ & Low-Level Questions (41-60)
    {"question": "What does the `volatile` keyword in C/C++ signify?",
     "options": ["a) The variable may change at any time", "b) The variable is stored in cache", "c) The variable is constant"], "correct": "a"},
    {"question": "What will be the output of this C expression?\n`sizeof(char) == sizeof(unsigned char)`",
     "options": ["a) depends on system", "b) false", "c) true"], "correct": "c"},
    {"question": "Which of these is a valid use of 'RAII' in C++?",
     "options": ["a) Manual memory management", "b) Using garbage collection", "c) Resource allocation in constructors"], "correct": "c"},
    {"question": "Which language feature in Rust ensures memory safety without GC?",
     "options": ["a) Threads", "b) Ownership", "c) Destructors"], "correct": "b"},
    {"question": "What is a memory leak?",
     "options": ["a) When memory is freed twice", "b) When memory size is exceeded", "c) When memory is not deallocated"], "correct": "c"},
    {"question": "What is the main purpose of `malloc` in C?",
     "options": ["a) To print memory address", "b) To free memory", "c) To allocate dynamic memory"], "correct": "c"},
    {"question": "What is a 'segmentation fault' in C/C++?",
     "options": ["a) An error caused by dividing by zero", "b) A network connection error", "c) An attempt to access restricted memory"], "correct": "c"},
    {"question": "What is the significance of `const` in C++?",
     "options": ["a) It defines a constant expression", "b) It prevents modification of a variable or object", "c) It makes a variable global"], "correct": "b"},
    {"question": "What is the output of `sizeof(int)` in C/C++?",
     "options": ["a) Always 8 bytes", "b) System-dependent", "c) Always 4 bytes"], "correct": "b"},
    {"question": "What is the purpose of a header file (.h) in C/C++?",
     "options": ["a) To store executable code", "b) To store source code for compilation", "c) To declare functions and variables"], "correct": "c"},
    {"question": "Which operator is used for dereferencing a pointer in C/C++?",
     "options": ["a) ->", "b) &", "c) *"], "correct": "c"},
    {"question": "What is the difference between `fork()` and `exec()` in Unix-like systems?",
     "options": ["a) `fork` replaces, `exec` creates", "b) Both create new processes", "c) `fork` creates a process, `exec` replaces it"], "correct": "c"},
    {"question": "What is an 'interrupt' in operating systems?",
     "options": ["a) A type of error in a program", "b) A signal to the CPU indicating an event", "c) A method to terminate a process"], "correct": "b"},
    {"question": "What is the purpose of `virtual` functions in C++?",
     "options": ["a) To prevent object instantiation", "b) To achieve runtime polymorphism", "c) To enable multiple inheritance"], "correct": "b"},
    {"question": "What is an 'endianness' problem?",
     "options": ["a) Order of execution of threads", "b) Order of bytes in memory", "c) Order of network packets"], "correct": "b"},
    {"question": "What is a 'daemon' in Unix-like systems?",
     "options": ["a) A user process that runs in the foreground", "b) A type of file system error", "c) A background process that runs without user interaction"], "correct": "c"},
    {"question": "What is the primary role of a 'compiler'?",
     "options": ["a) To debug code", "b) To execute code directly", "c) To translate high-level code into machine code"], "correct": "c"},
    {"question": "Which C++ standard library component is used for dynamic arrays?",
     "options": ["a) `std::array`", "b) `std::vector`", "c) `std::list`"], "correct": "b"},
    {"question": "What is a 'pointer' in C?",
     "options": ["a) A function that returns a memory address", "b) A variable that holds an integer value", "c) A variable that stores the memory address of another variable"], "correct": "c"},
    {"question": "What is the main difference between `new/delete` and `malloc/free` in C++?",
     "options": ["a) `new/delete` are faster", "b) `new/delete` handle objects, `malloc/free` handle raw memory", "c) `malloc/free` are C++ specific"], "correct": "b"},

    # Databases & SQL Questions (61-75)
    {"question": "In relational databases, what does the term 'normalization' mean?",
     "options": ["a) Adding indexes", "b) Removing redundancy", "c) Increasing redundancy"], "correct": "b"},
    {"question": "Which SQL isolation level prevents dirty reads?",
     "options": ["a) REPEATABLE READ", "b) READ UNCOMMITTED", "c) READ COMMITTED"], "correct": "c"},
    {"question": "What is the output of this SQL query?\n`SELECT NULL = NULL;`",
     "options": ["a) true", "b) unknown", "c) false"], "correct": "b"},
    {"question": "What is the main reason to use NoSQL databases over SQL?",
     "options": ["a) Fixed schema", "b) Flexible schema and horizontal scaling", "c) Strong typing"], "correct": "b"},
    {"question": "Which SQL keyword is used to retrieve data from a database?",
     "options": ["a) INSERT", "b) UPDATE", "c) SELECT"], "correct": "c"},
    {"question": "What is a 'primary key' in a relational database?",
     "options": ["a) A key used for encryption", "b) A column that uniquely identifies each record in a table", "c) A column that can contain duplicate values"], "correct": "b"},
    {"question": "What is a 'foreign key'?",
     "options": ["a) A unique identifier for a database", "b) A column that establishes a link between two tables", "c) A key used to secure data"], "correct": "b"},
    {"question": "What does ACID stand for in the context of database transactions?",
     "options": ["a) Analysis, Creation, Indexing, Deletion", "b) Atomicity, Consistency, Isolation, Durability", "c) Access, Control, Integrity, Data"], "correct": "b"},
    {"question": "Which type of join returns only the rows that have matching values in both tables?",
     "options": ["a) LEFT JOIN", "b) RIGHT JOIN", "c) INNER JOIN"], "correct": "c"},
    {"question": "What is 'indexing' in a database?",
     "options": ["a) A method to normalize data", "b) A data structure that improves the speed of data retrieval operations", "c) A way to encrypt data"], "correct": "b"},
    {"question": "What is 'denormalization' in databases?",
     "options": ["a) Introducing redundancy to improve performance", "b) Removing all relationships between tables", "c) The process of splitting tables into smaller ones"], "correct": "a"},
    {"question": "Which SQL clause is used to filter rows based on a specified condition?",
     "options": ["a) ORDER BY", "b) GROUP BY", "c) WHERE"], "correct": "c"},
    {"question": "What is a 'view' in SQL?",
     "options": ["a) A physical table storing data", "b) A virtual table based on the result-set of an SQL statement", "c) A user interface for database interaction"], "correct": "b"},
    {"question": "What is a 'deadlock' in databases?",
     "options": ["a) A database crash", "b) When a query runs indefinitely", "c) When two or more transactions are waiting for each other to release locks"], "correct": "c"},
    {"question": "What is the purpose of `COMMIT` in SQL?",
     "options": ["a) To delete a table", "b) To undo changes", "c) To save changes permanently to the database"], "correct": "c"},

    # Web Technologies & Networking Questions (76-90)
    {"question": "Which port does HTTPS use by default?",
     "options": ["a) 80", "b) 443", "c) 21"], "correct": "b"},
    {"question": "Which HTTP method is typically idempotent?",
     "options": ["a) POST", "b) GET", "c) PUT"], "correct": "c"},
    {"question": "Which network protocol is connection-oriented?",
     "options": ["a) UDP", "b) IP", "c) TCP"], "correct": "c"},
    {"question": "What is a 'race condition' in concurrent programming?",
     "options": ["a) A deadlock scenario", "b) When output depends on instruction execution order", "c) When threads compete for CPU time"], "correct": "b"},
    {"question": "What is 'CORS' in web development?",
     "options": ["a) Cascading Object Rendering Standard", "b) Cross-Origin Resource Sharing", "c) Client-Oriented Request System"], "correct": "b"},
    {"question": "Which of these is used for styling web pages?",
     "options": ["a) JavaScript", "b) HTML", "c) CSS"], "correct": "c"},
    {"question": "What is the primary role of 'JavaScript' in web development?",
     "options": ["a) Storing data on the server", "b) Defining page structure", "c) Adding interactivity to web pages"], "correct": "c"},
    {"question": "What is 'REST' in web services?",
     "options": ["a) A specific protocol like SOAP", "b) A database query language", "c) An architectural style for networked applications"], "correct": "c"},
    {"question": "What is the purpose of 'DNS'?",
     "options": ["a) To manage network security", "b) To translate domain names to IP addresses", "c) To encrypt network traffic"], "correct": "b"},
    {"question": "Which HTTP status code indicates a successful request?",
     "options": ["a) 404 Not Found", "b) 500 Internal Server Error", "c) 200 OK"], "correct": "c"},
    {"question": "What is a 'cookie' in web browsers?",
     "options": ["a) A type of malicious software", "b) A small piece of data sent from a website and stored on the user's computer", "c) A graphical user interface element"], "correct": "b"},
    {"question": "What is 'responsive web design'?",
     "options": ["a) Designing websites that respond quickly to user input", "b) Designing websites that store user preferences", "c) Designing websites that adapt to different screen sizes and devices"], "correct": "c"},
    {"question": "What is 'Webpack' commonly used for?",
     "options": ["a) Server-side rendering", "b) Database management", "c) Module bundling for web applications"], "correct": "c"},
    {"question": "What is the 'DOM' in web development?",
     "options": ["a) Data Order Management", "b) Direct Object Manipulation", "c) Document Object Model"], "correct": "c"},
    {"question": "Which protocol is used for secure communication over a computer network?",
     "options": ["a) HTTP", "b) HTTPS", "c) FTP"], "correct": "b"},

    # General Concepts & Operating Systems (91-100)
    {"question": "What is the primary function of an operating system's kernel?",
     "options": ["a) User interface management", "b) Application development", "c) Hardware resource management"], "correct": "c"},
    {"question": "What is 'virtual memory'?",
     "options": ["a) Memory that is not physically present", "b) Both a and b", "c) An extension of RAM using disk space"], "correct": "b"},
    {"question": "What is 'multithreading'?",
     "options": ["a) Running multiple processes on a single CPU core", "b) Running multiple programs simultaneously", "c) Running multiple parts of a program concurrently within the same process"], "correct": "c"},
    {"question": "What is a 'process' in operating systems?",
     "options": ["a) A static program stored on disk", "b) A collection of threads", "c) An instance of a computer program that is being executed"], "correct": "c"},
    {"question": "What is 'context switching'?",
     "options": ["a) Switching between different user accounts", "b) Changing the operating system settings", "c) The process of saving the state of one process and restoring the state of another"], "correct": "c"},
    {"question": "What is the purpose of a 'filesystem'?",
     "options": ["a) To handle process scheduling", "b) To manage network connections", "c) To organize and store data on storage devices"], "correct": "c"},
    {"question": "What is a 'firewall'?",
     "options": ["a) A device that amplifies network signals", "b) A tool for website development", "c) A network security system that monitors and controls incoming and outgoing network traffic"], "correct": "c"},
    {"question": "What is 'version control' primarily used for in software development?",
     "options": ["a) Optimizing code performance", "b) Testing software compatibility", "c) Tracking and managing changes to code"], "correct": "c"},
    {"question": "What is 'polymorphism' in object-oriented programming?",
     "options": ["a) The process of inheriting properties from multiple classes", "b) The ability of an object to take on many forms", "c) A method for data encapsulation"], "correct": "b"},
    {"question": "What is 'encapsulation' in object-oriented programming?",
     "options": ["a) Hiding implementation details from the user", "b) The process of breaking down a large program into smaller functions", "c) Bundling data and methods that operate on the data within a single unit"], "correct": "c"},

    # Hard questions (randomized)
    {
        "question": "**[Hard]** In a wait-free concurrent algorithm, which property strictly distinguishes it from lock-free algorithms?",
        "options": [
            "a) At least one thread will always make progress",
            "b) No operation can be preempted",
            "c) Every operation completes in a finite number of its own steps, regardless of other threads"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In the context of the Raft consensus algorithm, what is the main reason log compaction via snapshots is required?",
        "options": [
            "a) To guarantee linearizability under network partitions",
            "b) To reduce disk I/O latency for leader elections",
            "c) To prevent unbounded growth of the replicated log over time"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** Which of the following complexity classes is known to contain NP but is not known to be contained within PSPACE?",
        "options": [
            "a) EXPTIME",
            "b) PH (Polynomial Hierarchy)",
            "c) co-NP"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In virtual memory systems, what is the primary advantage of inverted page tables over conventional page tables?",
        "options": [
            "a) Faster address translation",
            "b) Reduced page fault rate",
            "c) Lower memory overhead for large address spaces"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In cryptography, why is the use of a nonce critical in AES-GCM mode?",
        "options": [
            "a) To ensure uniqueness of encryption for identical plaintexts",
            "b) To prevent key expansion",
            "c) To reduce the computational complexity of encryption"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** When designing a compiler, which phase is responsible for detecting variable type mismatches before code generation?",
        "options": [
            "a) Code optimization",
            "b) Lexical analysis",
            "c) Semantic analysis"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In TCP congestion control, what is the primary function of the 'slow start' phase?",
        "options": [
            "a) To reduce latency in packet delivery",
            "b) To gradually increase the congestion window to avoid overwhelming the network",
            "c) To immediately utilize maximum available bandwidth"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In distributed systems, what problem does the 'Byzantine Generals Problem' illustrate?",
        "options": [
            "a) Synchronizing processes in shared memory architectures",
            "b) Leader election under unreliable clocks",
            "c) Achieving consensus in the presence of arbitrary (malicious) failures"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** Which garbage collection algorithm is most suitable for systems with very short-lived objects and minimal pause times?",
        "options": [
            "a) Reference counting",
            "b) Mark-and-sweep",
            "c) Generational garbage collection"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In the Paxos consensus algorithm, what is the main role of the 'prepare' phase?",
        "options": [
            "a) To deliver committed values to all replicas",
            "b) To ensure no two different values can be chosen",
            "c) To elect a leader"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** Why are B+ trees preferred over B-trees in database indexing for range queries?",
        "options": [
            "a) They support faster insertion than B-trees",
            "b) All records are stored in the leaf nodes with linked pointers, enabling efficient range scans",
            "c) B+ trees require fewer disk accesses for random lookups"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In the context of CAP theorem, which two guarantees does a CP system provide?",
        "options": [
            "a) Consistency and Availability",
            "b) Availability and Partition tolerance",
            "c) Consistency and Partition tolerance"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** Which of the following scheduling algorithms can suffer from starvation if not carefully implemented?",
        "options": [
            "a) Round Robin",
            "b) First-Come, First-Served",
            "c) Priority Scheduling"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In operating systems, what is the main purpose of the Translation Lookaside Buffer (TLB)?",
        "options": [
            "a) To prefetch instructions for the CPU pipeline",
            "b) To store recently used virtual-to-physical address mappings",
            "c) To cache frequently accessed disk sectors"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In public-key cryptography, which problem is the RSA algorithm fundamentally based on?",
        "options": [
            "a) Elliptic curve point multiplication",
            "b) Integer factorization problem",
            "c) Discrete logarithm problem"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** Which data structure is best suited for implementing a priority queue with frequent decrease-key operations?",
        "options": [
            "a) Red-black tree",
            "b) Binary heap",
            "c) Fibonacci heap"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In database isolation levels, which anomaly is prevented by 'Repeatable Read' but not by 'Read Committed'?",
        "options": [
            "a) Phantom reads",
            "b) Dirty reads",
            "c) Non-repeatable reads"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In context of network routing, what does BGP primarily optimize for?",
        "options": [
            "a) Lowest latency route",
            "b) Shortest physical path",
            "c) Policy-based routing decisions"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** Why is tail-call optimization important in functional programming languages?",
        "options": [
            "a) It increases execution speed by skipping function calls",
            "b) It reduces stack usage for recursive functions",
            "c) It ensures constant-time execution of recursion"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In graph theory, which algorithm can be used to find strongly connected components in a directed graph?",
        "options": [
            "a) Prim's algorithm",
            "b) Dijkstra's algorithm",
            "c) Kosaraju's algorithm"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In the actor model of concurrency, how is state shared between actors?",
        "options": [
            "a) Through shared memory",
            "b) By message passing only",
            "c) Using global variables"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the primary security property provided by a cryptographic hash function?",
        "options": [
            "a) Key exchange",
            "b) Confidentiality",
            "c) Collision resistance"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** Which sorting algorithm has the best worst-case time complexity?",
        "options": [
            "a) BubbleSort",
            "b) QuickSort",
            "c) MergeSort"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In a context-free grammar, what does it mean if a grammar is ambiguous?",
        "options": [
            "a) It cannot generate all possible strings",
            "b) There exists at least one string with more than one distinct parse tree",
            "c) It generates an infinite language"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In machine learning, what is the primary difference between supervised and unsupervised learning?",
        "options": [
            "a) Supervised learning uses reinforcement",
            "b) Supervised learning requires labeled data, unsupervised does not",
            "c) Unsupervised learning predicts future events"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In the context of cache memory, what is the purpose of a write-back policy?",
        "options": [
            "a) To prevent cache misses",
            "b) To write data to main memory immediately",
            "c) To delay writing data to main memory until the cache block is replaced"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** What does the term 'eventual consistency' imply in distributed databases?",
        "options": [
            "a) Writes are immediately visible to all clients",
            "b) All nodes are always consistent",
            "c) Updates will propagate and all nodes will converge to the same state eventually"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In programming languages, what is a monad primarily used for?",
        "options": [
            "a) Defining syntax rules",
            "b) Handling side effects in functional programming",
            "c) Improving runtime performance"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In the context of computer networks, what is the primary role of the ARP protocol?",
        "options": [
            "a) Managing routing tables",
            "b) Resolving IP addresses to MAC addresses",
            "c) Encrypting data packets"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** Which of the following is a disadvantage of using linked lists compared to arrays?",
        "options": [
            "a) Higher memory locality",
            "b) Inefficient random access",
            "c) Fixed size"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In software testing, what does the term 'code coverage' measure?",
        "options": [
            "a) The performance of the software",
            "b) The percentage of code executed by tests",
            "c) The number of bugs found"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** Which type of database join returns all rows from the left table and matched rows from the right table?",
        "options": [
            "a) Inner join",
            "b) Right outer join",
            "c) Left outer join"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** What is the main benefit of static typing in programming languages?",
        "options": [
            "a) Improves runtime flexibility",
            "b) Allows variables to change type during execution",
            "c) Enables early detection of type errors at compile time"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In the OAuth 2.0 protocol, what is the role of the refresh token?",
        "options": [
            "a) To revoke access tokens",
            "b) To obtain a new access token without re-authentication",
            "c) To authorize resource access"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What does the 'no free lunch theorem' imply in optimization and machine learning?",
        "options": [
            "a) Optimization always requires free computational resources",
            "b) No algorithm is universally best for all problems",
            "c) Machine learning models never generalize well"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** Which method is commonly used to prevent deadlocks in operating systems?",
        "options": [
            "a) Round robin scheduling",
            "b) Priority scheduling",
            "c) Lock ordering"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In a relational database, what does normalization primarily aim to achieve?",
        "options": [
            "a) Speed up query execution",
            "b) Increase data redundancy",
            "c) Reduce data redundancy and improve data integrity"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** What is the key characteristic of a purely functional programming language?",
        "options": [
            "a) Uses imperative loops",
            "b) Functions have side effects",
            "c) Functions have no side effects and output depends only on input"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** What is the primary purpose of a memory barrier (fence) in concurrent programming?",
        "options": [
            "a) To allow out-of-order execution for optimization",
            "b) To allocate new memory dynamically",
            "c) To prevent memory operation reordering for correct synchronization"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In the TLS protocol, what cryptographic mechanism provides authentication of the server?",
        "options": [
            "a) Hash-based message authentication codes (HMAC)",
            "b) Symmetric encryption with a shared key",
            "c) Digital certificates signed by a trusted certificate authority"
        ],
        "correct": "c"
    },

    # Modern Web Development & Frameworks (New Questions)
    {
        "question": "**[Hard]** In React, what is the primary purpose of the useEffect cleanup function?",
        "options": [
            "a) To prevent memory leaks by cleaning up subscriptions and timers",
            "b) To clear component state before re-rendering",
            "c) To optimize render performance"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** What is the main difference between Server-Side Rendering (SSR) and Static Site Generation (SSG)?",
        "options": [
            "a) SSR generates pages at request time, SSG generates pages at build time",
            "b) SSR is faster than SSG",
            "c) SSG requires a server, SSR doesn't"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** In GraphQL, what problem does the DataLoader pattern solve?",
        "options": [
            "a) Authentication issues",
            "b) The N+1 query problem through batching and caching",
            "c) Type safety enforcement"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the primary benefit of using Virtual DOM in React?",
        "options": [
            "a) Direct manipulation of browser DOM",
            "b) Efficient reconciliation and minimal DOM updates",
            "c) Automatic state management"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In Node.js, what is the event loop primarily responsible for?",
        "options": [
            "a) Managing CPU-intensive computations",
            "b) Handling asynchronous operations and callbacks",
            "c) Garbage collection"
        ],
        "correct": "b"
    },

    # Cloud Computing & DevOps
    {
        "question": "**[Hard]** In Docker, what is the primary difference between a container and an image?",
        "options": [
            "a) Containers are mutable runtime instances, images are immutable templates",
            "b) Images run code, containers store code",
            "c) Containers are stored on disk, images run in memory"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** What does Kubernetes use 'etcd' for?",
        "options": [
            "a) Container runtime",
            "b) Load balancing",
            "c) Distributed key-value store for cluster state"
        ],
        "correct": "c"
    },
    {
        "question": "**[Hard]** In microservices architecture, what is the purpose of a service mesh?",
        "options": [
            "a) To manage database connections",
            "b) To handle service-to-service communication, security, and observability",
            "c) To deploy containers"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the primary advantage of using Infrastructure as Code (IaC)?",
        "options": [
            "a) Faster code execution",
            "b) Version control and reproducibility of infrastructure",
            "c) Automatic security patching"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In AWS, what is the primary use case for Lambda functions?",
        "options": [
            "a) Long-running background processes",
            "b) Serverless, event-driven compute execution",
            "c) Database hosting"
        ],
        "correct": "b"
    },

    # Security & Authentication
    {
        "question": "**[Hard]** What vulnerability does CSRF (Cross-Site Request Forgery) exploit?",
        "options": [
            "a) SQL injection in forms",
            "b) The browser's automatic inclusion of cookies with requests",
            "c) Weak password policies"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the primary purpose of salting passwords before hashing?",
        "options": [
            "a) To make passwords longer",
            "b) To prevent rainbow table attacks and ensure unique hashes",
            "c) To encrypt the password"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In JWT (JSON Web Tokens), what does the signature verify?",
        "options": [
            "a) The user's password",
            "b) That the token hasn't been tampered with and was issued by a trusted source",
            "c) The token expiration time"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What type of attack does Content Security Policy (CSP) primarily prevent?",
        "options": [
            "a) SQL injection",
            "b) Cross-Site Scripting (XSS)",
            "c) DDoS attacks"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the difference between symmetric and asymmetric encryption?",
        "options": [
            "a) Symmetric uses one key, asymmetric uses a key pair (public/private)",
            "b) Symmetric is slower than asymmetric",
            "c) Asymmetric can only decrypt, not encrypt"
        ],
        "correct": "a"
    },

    # Design Patterns & Architecture
    {
        "question": "**[Hard]** What problem does the Singleton pattern solve?",
        "options": [
            "a) Ensuring multiple instances of a class",
            "b) Ensuring only one instance of a class exists",
            "c) Managing object inheritance"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In the Observer pattern, what is the role of the Subject?",
        "options": [
            "a) To observe changes in other objects",
            "b) To notify registered observers when its state changes",
            "c) To create new observer instances"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the main principle behind the Repository pattern?",
        "options": [
            "a) Direct database access from UI",
            "b) Abstracting data access logic from business logic",
            "c) Storing data in memory cache"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In SOLID principles, what does the 'L' (Liskov Substitution Principle) state?",
        "options": [
            "a) Large classes should be split into smaller ones",
            "b) Subtypes must be substitutable for their base types without altering correctness",
            "c) Classes should depend on abstractions"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the primary benefit of the Factory pattern?",
        "options": [
            "a) Faster object creation",
            "b) Encapsulating object creation logic and decoupling from concrete classes",
            "c) Automatic garbage collection"
        ],
        "correct": "b"
    },

    # Advanced Python
    {
        "question": "**[Hard]** What is the purpose of Python's `__slots__`?",
        "options": [
            "a) To define private methods",
            "b) To reduce memory usage by preventing dynamic attribute creation",
            "c) To enable multiple inheritance"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In Python, what is the difference between `@classmethod` and `@staticmethod`?",
        "options": [
            "a) @classmethod receives the class as first argument, @staticmethod doesn't receive implicit arguments",
            "b) They are identical",
            "c) @staticmethod can modify class state"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** What does Python's `with` statement guarantee?",
        "options": [
            "a) Faster code execution",
            "b) Proper resource cleanup via context manager protocol",
            "c) Thread safety"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is a Python descriptor?",
        "options": [
            "a) A documentation string",
            "b) An object that defines __get__, __set__, or __delete__ methods",
            "c) A type annotation"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the purpose of `asyncio.gather()` in Python?",
        "options": [
            "a) To collect garbage",
            "b) To run multiple coroutines concurrently and collect results",
            "c) To synchronize threads"
        ],
        "correct": "b"
    },

    # Advanced JavaScript/TypeScript
    {
        "question": "**[Hard]** In JavaScript, what does 'closure' refer to?",
        "options": [
            "a) Ending a function with a return statement",
            "b) A function that has access to variables in its outer (enclosing) scope",
            "c) Closing database connections"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the difference between `null` and `undefined` in JavaScript?",
        "options": [
            "a) They are identical",
            "b) `undefined` is uninitialized, `null` is explicitly assigned absence of value",
            "c) `null` is a syntax error"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What does the JavaScript `Promise.race()` method do?",
        "options": [
            "a) Waits for all promises to resolve",
            "b) Returns the result of the first promise to settle (resolve or reject)",
            "c) Cancels all promises except the fastest"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In TypeScript, what is a 'discriminated union'?",
        "options": [
            "a) A union of classes",
            "b) A union type with a common property used for type narrowing",
            "c) A deprecated feature"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the purpose of JavaScript's `WeakMap`?",
        "options": [
            "a) To store weak passwords",
            "b) To hold weak references to objects allowing garbage collection",
            "c) A less performant version of Map"
        ],
        "correct": "b"
    },

    # System Design & Architecture
    {
        "question": "**[Hard]** What is the primary purpose of a load balancer?",
        "options": [
            "a) To store user data",
            "b) To distribute incoming traffic across multiple servers",
            "c) To cache database queries"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In caching strategies, what does 'cache aside' (lazy loading) mean?",
        "options": [
            "a) Cache is always synchronized with database",
            "b) Application checks cache first, loads from DB on miss and updates cache",
            "c) Cache is never used"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What problem does database sharding solve?",
        "options": [
            "a) Data redundancy",
            "b) Horizontal scaling by partitioning data across multiple databases",
            "c) Vertical scaling"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the main trade-off of using a Content Delivery Network (CDN)?",
        "options": [
            "a) Reduced latency for static content vs. additional cost and complexity",
            "b) Faster database queries",
            "c) Better security vs. slower performance"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** In distributed systems, what is 'idempotence'?",
        "options": [
            "a) The ability to scale vertically",
            "b) An operation that produces the same result when executed multiple times",
            "c) Immediate consistency"
        ],
        "correct": "b"
    },

    # Git & Version Control
    {
        "question": "**[Hard]** What is the difference between `git merge` and `git rebase`?",
        "options": [
            "a) Merge creates a new commit, rebase rewrites commit history",
            "b) They are identical",
            "c) Rebase is slower than merge"
        ],
        "correct": "a"
    },
    {
        "question": "**[Hard]** What does `git cherry-pick` do?",
        "options": [
            "a) Deletes specific commits",
            "b) Applies a specific commit from one branch to another",
            "c) Merges all branches"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In Git, what is the purpose of a 'tag'?",
        "options": [
            "a) To mark a specific point in history, typically for releases",
            "b) To create a new branch",
            "c) To resolve merge conflicts"
        ],
        "correct": "a"
    },

    # API Design & REST
    {
        "question": "**[Hard]** What HTTP status code should be returned for a successful resource creation?",
        "options": [
            "a) 200 OK",
            "b) 201 Created",
            "c) 204 No Content"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** In REST API design, what is the principle of 'statelessness'?",
        "options": [
            "a) Server doesn't store session data",
            "b) Each request contains all information needed to process it",
            "c) APIs don't use databases"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the purpose of API rate limiting?",
        "options": [
            "a) To slow down all requests",
            "b) To prevent abuse and ensure fair usage of resources",
            "c) To improve response time"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is HATEOAS in REST architecture?",
        "options": [
            "a) A security protocol",
            "b) Hypermedia As The Engine Of Application State - responses include links to related resources",
            "c) A database query language"
        ],
        "correct": "b"
    },

    # Performance & Optimization
    {
        "question": "**[Hard]** What is 'lazy loading' in web development?",
        "options": [
            "a) Slow code execution",
            "b) Deferring loading of non-critical resources until needed",
            "c) Loading all resources at startup"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the purpose of database indexing?",
        "options": [
            "a) To backup data",
            "b) To speed up data retrieval operations at the cost of write performance",
            "c) To delete old records"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is 'code splitting' in modern web applications?",
        "options": [
            "a) Dividing code into multiple files for better organization",
            "b) Breaking up code bundles to be loaded on demand",
            "c) Using multiple programming languages"
        ],
        "correct": "b"
    },
    {
        "question": "**[Hard]** What is the benefit of using CDN for static assets?",
        "options": [
            "a) Cheaper hosting",
            "b) Reduced latency by serving content from geographically closer servers",
            "c) Better security only"
        ],
        "correct": "b"
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