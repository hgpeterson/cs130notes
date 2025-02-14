# Program Usability (Part 1)

## Usability

What makes a program "usable"?

- Usability is all about how easy it is for users to perform tasks

    - How easy is it to learn how to perform a task?

    - How efficient is it to perform a task (e.g., how many steps must the user perform)?

    - Can the program be customized or adapted to allow users to work more efficiently?

    - Does the program take steps to reduce the impact of errors or features?

**Usability has a *profound* effect on the perceived quality of software!**

Techniques for making it easier to learn how to complete tasks:

- Tip of the Day, UI tooltips, command-line help output, man pages

Techniques for improving task efficiency:

- Accessible tools for common operations, keyboard shortcuts, default values for configuration options

Techniques for customizing or adapting to the user to improve their efficiency:

- Advanced configuration, dockable widgets and menus, ability to create macros, support for plugins or custom commands

Techniques for reducing impact of user errors:

- Detect bad inputs early, allow users to correct bad inputs, confirmation dialogues, "undo" or "redo" support, ability to "cancel" long-running operations

Techniques for reducing impact of application and system errors:

- Autosave to avoid data loss, transacted operations to avoid corruption, ability to migrate data from earlier versions of software

### Architecture/Design

Achieving usability often requires multiple design iterations, giving users prototypes to work with, and getting user feedback.

> *"One of the most helpful things an architect can do to make a system usable is to facilitate experimentation with the user interface via the construction of rapid prototypes.  Building a prototype, or several prototypes, to let real users experience the interface and give their feedback pays enormous dividends.  The best way to do this is to design the software so that the user interface can be quickly changed."*

—*Software Architecture in Practice* 3rd ed., pg. 178

## Principles of Program Design

### The KISS Principle

**Keep It Simple, Stupid.**

> *"Everyone knows that debugging is twice as hard as writing a program in the first place.  So if you’re as clever as you can be when you write it, how will you ever debug it?"*

—Brian Kernighan, coauthor of The C Programming Language and creator of many standard UNIX programs

- Simple systems are easier to correct

- Gravitate towards the simplest conceptual models that include all the essential details

### ETE, HTP

**Easy things should be easy, hard things should be possible.**

> *"Perl is a language for getting your job done. Of course, if your job is programming, you can get your job done with any “complete” computer language, theoretically speaking.  But we know from experience that computer languages differ not so much in what they make possible, but in what they make easy.  At one extreme, the so-called “fourth generation languages” make it easy to do some things, but nearly impossible to do other things. At the other extreme, certain well known, “industrial-strength” languages make it equally difficult to do almost everything.Perl is different. In a nutshell, Perl is designed to make the easy jobs easy, without making the hard jobs impossible.*

—*Programming Perl*, 2nd ed. by Larry Wall

- User interfaces should make the basic, common tasks as effortless as possible

- Don't design your UI around the most advanced tasks!

    - Even advanced users appreciate a clean, simple UI that works efficiently

- Internal and external APIs should also make basic, common tasks effortless

- If an operation can have "simple" and "advanced" versions:

    - Some languages support optional arguments, which can control more advanced, less common functionality

    - Some APIs provide "basic" and "advanced" versions of API calls (e.g., Windows API has `CopyFile` and `CopyFileEx`)

- Also consider setup and teardown for common programming tasks

    - If you expect users to do certain things a lot, make it easy for them!

*Donnie Tip:* Writing tests will help you realize what's easy/hard to do with your program!

### Fail Fast and Visibly

**When software encounters a fatal error, it should fail fast and visibly.**

- Use assertions liberally in your program

    - You can turn them off later if you're worried about the overhead
    
    - Corollary: make sure you do important operations *outside* of assertions, and then only use assertions to verify the state

- Check arguments

*Donnie Tip:* When there is a program-killing bug in the code, the longer it takes for the program to die, the harder it will be to find the bug!

Are there worse things than a program hitting a bug and crashing?
Application health hierarchy (Mike Stall, via Jeff Atwood):

1. Application works as expected and never crashes

2. Application crashes due to rare bugs that nobody notices or cares about

3. Application crashes due to a commonly encountered bug

4. Application deadlocks and stops responding due to a common bug

5. Application crashes long after the original bug

6. Application causes data loss and/or corruption

Generally, the most undesirable behaviors happen when:

1. Programmers either ignore or mask errors that occur in their programs

2. Programmers try to be too clever in how they handle error conditions

In the code you write:

- Always check return-codes of functions (e.g. for UNIX syscalls)

    - If a call fails, always report it via exception or error-logging

- Be realistic about the kinds of errors you can *actually* resolve in you code

    - If there isn't a simple and clear way to resolve an error, it's probably better to just fail

- *Never* silently swallow exceptions, even when they are "never expected"—always at least log (or otherwise report) the error

- Be simple (KISS) about how you manage internal program state—make assertions and/or report exceptions when expections are not met

When you design APIs and functions:

- Check all arguments for validity up front. 

    -If an argument is bad, your exception message should be clear and specific (e.g., "Scale must be a value in range [0, 1]; got -567898765.2")

- Don't change any program state or start long-running tasks until you have completed all fast and easy argument checks!

    - Example: Do some checks on how much memory will be needed and report it so that the user can kill the task early.

## Command-Line Programs

Command-line (CLI) programs are a very common implementation approach and are often preferred by more advanced users.

### The UNIX Philosophy

Build **"small, sharp tools"** (Peter H. Salus):

1. Write programs that do one thing and do it well

2. Write programs to work together

3. Write programs to handle text streams, because that is a universal interface

### Tools with Subcommands

Obvious example: `git`.

### Patterns

- **Always** provide some built-in usage help to the user (e.g., `git help`)

- Try to use the same command-line arguments that other similar tools also use (e.g., `-v` for verbose output)

- Use standard argument-parsing libraries (e.g., `argparse` in Python)