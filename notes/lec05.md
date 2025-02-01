# GRASP

General Responsibility Assignment Software Principles: A set of principles that direct the design of software systems

## Responsibilities of the software

How do we *assign responsibilities* to pieces of code?
Two types:
1. **Doing**: some action must be carried out
2. **Knowing**: some information must be maintained

*Donnie tip:* Don't fall into the trap of "I don't know enough about the problem/what to do, so I won't do anything yet"!

> *"Prepare to throw the first try away."* — Fred Brooks

The effort of attempting to build something will teach you. Don't get stuck in *analysis paralysis*.

## Coupling

**Coupling** is a qualitative measure of how strongly one component is connected to, has knowledge of, or depends on other components.

- If coupling is high, changes in one component are likely to require changes in another 🙁

Example: Class hierarchies have a high coupling.

> A guiding principle of GRASP is *low coupling*.

## Cohesion

**Cohesion** is a qualitative measure of how functionally related the various operations of a single component are to each other

- How broad/specific is the focus of the software component?

- Cohesion can be thought of as intra-component coupling

When cohesion in a component is low:
- it's hard to understand
- reuse of functionality is less likely (because it's hard to find)
- changes made to the component are likely to have unintended consequences

Low cohesion and high coupling often accompany each other
- will want to **refactor** (change structure of code without changing its observed behavior)

> GRASP principle: *High Cohesion*

## Information expert

> *Always assign the responsibility to a class that has the information needed to fulfill it.*

Example: Should the `Workbook`, `Sheet`, or `Cell` class compute a cell value based on its contents?

Following this principle will help increase cohesion.

## Creator

Who should be responsible for creating a new instance of some class? (Example: who should create a new sheet? A new cell?)

> *Assign component C1 the responsibility to create an instance of C2 if one+ of these is true:*
> - *C1 contains aggregates of C2*
> - *C1 records C2*
> - *C1 closely uses C2*
> - *C1 has the initializing data for C2*

If multiple implementations of C2 are possible, may need a different approach, e.g. Dependency Inversion Pattern (SOLID), or C2 class hierarchy.

## User interfaces

From *Software Architecture in Practice* 3rd ed., pg. 178:
> *"One of the most helpful things an architect can do to make a system usable is to facilitate experimentation with the user interface via the construction of rapid prototypes. Building a prototype, or several prototypes, to let real users experience the interface and give their feedback pays enormous dividends. The best way to do this is to design the software so that the user interface can be quickly changed."*

Remember: need **low coupling** between user-interface code and application logic.

## Controller

What first object beyond the UI layer receives the coordinates ("controls") a system operation?

> *Assign the responsibility to a component representing one of these choices:*
> - *A component that represents the overall "system", a "root object," a specialized hardware device that the software is running within (e.g. an ATM), or a major subsystem (all variations of a façade controller)*
> - *A component that represents a specific use-case scenario within which the system operation occurs (a use-case controller or session controller)*

Examples: 
- A spreadsheet workbook
- A compiler driver (in compiled languages)

The controller should **not** contain domain logic (Example: finding cycles in a sheet).
Instead, it should direct *subsystems* to perform the appropriate operations.

## Polymorphism

*Polymorphism* is when the behavior of the code changes based on the types of objects involved.

Example: `Shape` class with `getArea()` method.
Should be different for, e.g., `Rectangle` and `Circle` subclasses.

> *Don't make leaky abstractions! Assign responsibility for behavior to the types for which the behavior varies.*

Example: Don't have a `getTotalArea()` function have an `if-else` block that does something different for every shape!

Note: Sometimes there is no clear benefit of creating a type hierarchy... Example: converting between t