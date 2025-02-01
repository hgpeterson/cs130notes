# Software Performance Measurement and Tuning (Part 1)

It's hard to guess where performance issues actually are.
That's what benchmarking tools are for!

## Program Performance

Program performance (in, e.g., time-to-execute, memory usage, etc.) usually becomes a consideration at some point during a software project lifecycle.

> *"Premature optimization is the root of all evil"* —Donald Knuth

Improving program performance carries a risk of reducing other quality attributes (readability, modifiability, debuggability).
It may not be as important as you think; as always, start with the requirements!

Aim for SMART performance goals:
- Specific
- Measurable
- Achievable
- Relevant
- Time-limited

"As fast as possible" is great, but a specific, measurable goal will let you know when you're finished.

Performance can be affected at many levels of a project:
- Software requirements and quality attributes (how precise does the calculation need to be?)
- Program architecture and design
    - Choices of algorithms, data structures, parallelism
- Platform
    - Programming language choices (compiled vs. interpreted, optimizing compilers)
    - Operating systems
- Hardware (faster/more processors, GPUs, more memory, faster storage devices, faster networks)
- Code tuning

Developers can make a mistake by only focusing on *code tuning.*

## Multi-Level Performance Improvement

Reddy & Newell, 1997: *Multiplicative Speedup of Systems*.
- Performance improvements often multiply across levels


## Physical Simulation and Performance

Appel, 1985: *"An Efficient Program for Many-Body Simulation*.

Improvements from the $O(N^2)$ $N$-body problem:

| Design Level                   | Speedup Factor |
|--------------------------------|----------------|
| Algorithms and Data Structures | 12x            |
| Algorithm Tuning               | 2x             |
| Data Structure Reorganization  | 2x             |
| System-Independent Code Tuning | 2x             |
| System-Dependent Code Tuning   | 2.5x           |
| Hardware                       | 2x             |
| **Total**                      | **480x**       |

**Understanding the problem deeply results in higher-performance programs.**

## Design

This is where you are likely to achieve the greatest benefits. 
Don't get stuck in analysis paralysis, but it's worth thinking deeply about the problem before you code.
And don't be afraid of starting over if a better idea comes along!

## Computer Architecture

Design and implement to the computer's strengths!

Example 1:
- Memory access: 1 to 100 ns
- SSD access: 10 to 100 us
- HDD access: 1 to 10 ms

Example 2: Dynamic memory management is slow
- Only use when necessary
- Prefer fewer larger allocations rather than many small allocations
- If many small allocations is unavoidable, consider a pooled-object allocator

## Algorithms and Data Structures

Choose algorithms and data structures that are as complex as necessary, but *not more complicated!*
- Consider expected data volumes, necessary operations, etc.
- Use a simple solution if possible

Example: Managing a queue of elements
- Need to push elements on the back of the queue, pop elements off the front
- For small number of elements, an array-backed implementation is actually faster and much simpler to reason about

## Coding Style

Focus on writing clear and understandable code rather than writing the fastest possible program.
Compilers and interpreters often include optimizations for common language idioms.

Do regular performance testing to identify whether you are meeting your performance requirements!

## Measurement

Use tools to identify performance issues; *Don't guess!*
- Use code profilers to identify **hot spots** in your code
- Use memory heap analyzers to identify what objects take up the most space
- Consider building performance measurement functionality into the code itself and logging info at run-time

### Profiling Techniques

1. **Instrumenting profilers** modify the program code to record what code is being executed
    - Very accurate, but slow
2. **Sampling profilers** periodically interrupt the program in execution, analyzing its current execution state
    - Imprecise, but fast
3. Emulation
4. Hardware Performance Counters

### Accuracy

**Wall-clock time** = the actual amount of time it takes to run a program
- Pros: Easy to compute, reflects user's perspective
- Cons: Not representative of what program is doing (it could just be waiting on I/O, for instance)

**CPU time** = the time your program actually spends on the CPU
- Tracked by OS kernel
- Can be broken down into time spent in program vs. time spent in kernel on behalf of program

Generally, you want to perform an operation many times, measure the total time, and then divide by the number of repetitions to get a more accurate measurement.
Why? Because repeated measurements of an operation can vary significantly as the computer does all kinds of other stuff like caching data, precompiling, etc.
- Python: see the `timeit` module

Keep a log of the changes you make and their impact!

## Example

See pages 605 and 606 of Steve McConnell's *Code Complete* (2nd ed.).