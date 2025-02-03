# Software Performance Measurement and Tuning (Part 2)

## Donald Knuth on Performance

In 1971, Donald Knuth looked at many Fortran programs and found that, "less than 4% of a program generally accounts for about half of its running time."

One of his famous quotes:

> *"Premature optimization is the root of all evil"*

from Knuth, 1974: *Structured Programming with go to Statements*.

But he *does not* advocate ignoring performance considerations.

The full quote has more context:

> *"There is no doubt that the grail of efficiency leads to abuse.  Programmers waste 
enormous amounts of time thinking about, or worrying about, the speed of noncritical 
parts of their programs, and these attempts at efficiency actually have a strong 
negative impact when debugging and maintenance are considered.  We should forget 
about small efficiencies, say about 97% of the time:  premature optimization is the root 
of all evil.*

> *Yet we should not pass up our opportunities in that critical 3%.  A good programmer 
will not be lulled into complacency by such reasoning, he will be wise to look carefully 
at the critical code; but only after that code has been identified.  It is often a mistake to 
make a priori judgments about what parts of a program are really critical, since the 
universal experience of programmers who have been using measurement tools has 
been that their intuitive guesses fail. . ."*

So we should make sure we are optimizing in a *structured way* because humans are bad at knowing where the code will be slow!

## Computer Architecture

Understanding the computer's architecture can help you understand how to achieve better program performance.

- Different buses and devices have different throughputs and latencies

- If a program uses part of the computer heavily, its maximum speed can become limited by that component's performance (we call this a **bottleneck** and that the program is **bound** by that component, e.g., *"CPU-bound"*)

- Sometimes a program can be changed to rely less heavily on the component (e.g., cache disk data in memory to reduce disk IO overhead)

## Program Optimization

Some approaches can improve performance regardless of the bottleneck

- Improve the relevant computer hardware

- Find ways to reduce the program's usage of the computing resource

- Caching

Beyond that, different bottlenecks will dictated what approaches are best.

### CPU Utilization

A **CPU-bound** program can be modified to use multiple processors

- Run multiple instances of the program in different processes to compute *non-overlapping* parts of the problem (easy)

- Use multiple threads of execution to run on multiple processors in parallel (hard)

Terminology:

- **Parallel** = different code running on different processes

- **Concurrent** = one processes switching between different bits of code

*Issue:* multi-threading imposes an overhead on program execution (context-switches, lock contention, etc.)

**Amdahl's Law:**

> *"If your program has some part that **must** be done sequentially, the sequaential part limits the benefit of parallelization.*

The speedup due to parallelizing on $N$ CPUs will be $(S + (1 - S) / N)^{-1}$ where $S$ is the percentage of the task that must be run sequentially. (Ex: for $S$ = 10%, only 4.7x speedup on 8 CPUs 🙁. . . even as $N \to \infty$ the speedup goes to only 10x!)

Often times, when one increases the **size** of the problem, the parallel part grow faster than the sequential part, in which case parallelizing is more valuable for larger problems (see **Gustafson—Barsis' Law**)

Some terminology:

- **Strong scaling** = How the program speed scales with parallelization

- **Weak scaling** = How the program speed scales with size of the problem

### I/O Utilization

**I/O-bound** programs can use various techniques to improve performance:

- Caching data is a common solution, especially for disk I/O

- With Network I/O, there may be either CPU bottlenecks or networking bottlenecks at local and/or remote servers

    - Networked programs often benefit greatly from multithreading (one thread per connection with remote system)

    - Modern web servers use something called *socket polling*, which scales even faster using OS calls that efficiently monitor a large collection of sockets from one thread

### Platforms

Python:

- API supports multiple threads of execution, but the global interpreter lock (GIL) prevents two Python threads from ever executing at the same time (this may change for 3.13+)

- CPython also switches between threads on a regular basis, so locks must still be used to guard shared states

- So, Python threading is basically useless for CPU bottlenecks. . . but it still works well for network bottlenecks

- Libraries like NumPy and Numba are implemented in C with Python wrappers

    - They can use multithreading (using OpenMP/OpenACC in C) because the GIL is released when you call them

- Using the `multiproccessing` module, you can spawn OS-level processes which can run on different CPUs

    - Since the processes don't share the same address space, must solve the problem of passing information between processes

## Case Study: Windows Terminal vs. `Refterm`

Casey Muratori (game developer) [complained about the performance of Windows Terminal](https://github.com/microsoft/terminal/issues/10362)

- Response from Microsoft devs was that it would be an impossibly large amount of work to improve the Windows Terminal performance

- Casey wrote a "reference terminal" over two weekends that was 1000x faster

    - [Video 1](https://www.youtube.com/watch?v=hxM8QmyZXtg)
    - [Video 2](https://www.youtube.com/watch?v=99dKzubvpKE)

- He even made a five-part series: 
    
    - [Part 1: Philosophies of Optimization](https://www.youtube.com/watch?v=pgoetgxecw8)

    - [Part 2: Slow Code Isolation](https://www.youtube.com/watch?v=lStYLF6Us_Q)

    - [Part 3: Minimal Buffer Processing](https://www.youtube.com/watch?v=hNZF81VYfQo)

    - [Part 4: Glyph Hash Table](https://www.youtube.com/watch?v=cGoQ3ceKX6g)

    - [Part 5: Parsing with SIMD](https://www.youtube.com/watch?v=e1cvqmXoVaI)