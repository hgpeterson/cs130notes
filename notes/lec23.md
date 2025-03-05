# Software Design Principles: The SOLID Principles

**For most software, the most critical QA is *modifiability*.**
A set of five principles called **SOLID** have been proposed by Robert C. "Uncle Bob" Martin to guid software architectural/design choices.

> *"The goal of the principles is the creation of mid-level software structures that tolerate change, are easy to understand, and are the basis of components that can be used in many software systems"* (*Clean Architecture*, pg. 58)

The SOLID principles are most relevant to module-level code, but can be applied at every level of software design.
They are also focused on OOP, but can be applied in other contexts as well.

Let's go through the five principles:

1. SRP: Single Responsibility Principle
2. OCP: Open-Closed Principle
3. LSP: Liskov Substitution Principle
4. ISP: Interface Segregation Principle
5. DIP: Dependency Inversion Principle

## Single Responsibility Principle

Originally, SRP was stated as, "A module should have one, and only one, reason to change."
Now, it is more common to say, **"A module should be responsible for one, and only one, actor."**
If a module contains code that supports multiple actors or roles,
- Different actors don't always require changes at the same time, or for the same reasons, but the code supporting those actors is in close proximity
- Often, code supporting different actors actually becomes coupled together

**Goal:** Separate code that supports different actors so that their requirements can change independently.

**Example**: an `Employee` class used in business management
- Accounting needs to know how much to pay employees
    - `computePay()` will calculate this amount
- HR wants to know how much everyone is working
    - `reportHours()` will handle this
- Both operations can call `regularHours()` to compute the number of hours worked. . .
- *Problem:* HR and Accounting don't necessarily have the same definitions for "how many hours an employee works" (e.g., what counts as "regular hours" vs "overtime"?)
    - If the programmer changes the implementation of `regularHours()` to match some change that *only* Accounting *or* HR needs, the change will affect *both* HR *and* Accounting
- A better design is to separate the code based on Actors using it
    - A basic `Employee` class that tracks "ground truth" data
    - Additional classes (like `PayCalculator` and `WorkplaceHealthReport`) to handle responsibilities for different Actors, e.g., that take an `Employee` object as argument
    - This makes it clear the the `Employee` class must have a stable implementation because multiple features depend on it!

## Open-Closed Principle

OCP was first stated by Bertrand Meyer in 1988: "A software artifact should be open for extension but closed for modification."
In other words, it should be possible to extend the behavior of a software component without modifying the code itself.

**Example:** Need to generate financial reports to display on the web
- Negative financial amounts are displayed in *red*
- Later, want to generate financial reports to print, so negative financial amounts are displayed using *parentheses*
- *How much code needs to change to implement this new feature?*
    - If the entire web report generator is encapsulated in one class, we will have to do a significant amount of refactoring
    - Better architecture: break the implementation into multiple steps:
        - `ReportCalculator`, `ReportData`, and `ReportPresenter`, where the last one can have both the `WebReportPresenter` and the `PrintReportPresenter` implementations
        - The key idea behind OCP is that the `ReportPresenter` interface should be unlikely to change, while the `WebReportPresenter` and `PrintReportPresenter` implementations *are* likely to change

## Liskov Substitution Principle

LSP was first stated by Barbara Liskov in 1988.
Roughly stated: "If `S` is a subtype of `T`, then it should be possible to substitute object of type `S` into a program that uses type `T` without adversely affecting the correctness of the program."

**Example:** A simple `Rectangle` class and a program that uses it
```
Rectangle r = ...
r.setWidth(5)
r.setHeight(2)
assert r.getArea() == 10
```
- Add a `Square` subclass to `Rectangle` which additionally enforces that the width and height are always equal
- Does the above program continue to work if we make `r` a `Square` instead of a `Rectangle`?
    - No. Need to change `assert r.getArea() == 10` to `assert r.getArea() == 4` if `r` was a `Square`. This means we have a *leaky abstraction* 

In general LSP violations occur because a subclass or an interface implementation doesn't conform to all super-type expectations.
- The subtype must accept all of the inputs that the super-type accepts
- The subtype must not generate outputs that conflict with any super-type constraints on output
- The subtype must conform to all invariants that the super-type expects to hold

In the example above, the problem is that `setHeight()` and `setWidth()` are no longer independent in the `Square` subtype.
A better abstraction would be a more general `Shape`.

## Interface Segregation Principle

ISP: "Clients should not be forced to depend on operations they do not use."
- In this context, "depend on" really means "be aware of," "be exposed to," etc.

**Example:** a Calculator program with multiple modes
- Could specify a single **fat interface** that includes all operations that the calculator can perform, but this can create problems for both users and implementers!
    - Interface users must understand a complex abstraction that doesn't focus only on the problem they want to solve
    - Interface implementers may only want to provide a subset of operations
- A much better approach would be to break the interface into multiple smaller **role interfaces** `BasicCalculator`, `ScientificCalculator`, `ProgrammingCalculator`
    - Each interface focuses on the needs of a single actor/role
    - Now users can use the interface that best matches their problem
    - Implementers can implement only the operations needed for the role
- Smaller role-based interfaces also insulate against changes. Imagine we want to have a graphing calculator mode.
    - If we add graphing function to a fat Calculator interface, existing implementations would now be broken because they are missing required functions
    - This is also a violation of the SRP—the Actor that requires graphing support is very different from the Actor that requires basic calculator support


## Dependency Inversion Principle

DIP is stated as "High-level modules should not depend on low-level modules. Both should depend on abstractions."
Put another way, "Abstractions should not depend on details. Details should depend on abstractions."

**Example:** A common way to structure purpose-built programs is with three levels:
- `Policy` = what the program does
- `Mechanism` = how the program does it
- `Utility` = common routines

This way, the higher-level code (`Policy`) has a *dependency* on the lower-level code (`Utilities`).
- Not inherently bad, but it makes the program **hard to change**
- DIP recommends: 
    - Have the higher-level code specify its needs/requirements on the lower-level code by way of interfaces/abstractions, and have the lower-level code implement those abstractions
    - So make `Mechanism` and `Utility` «interfaces»
    - `MechanismImpl` implements `Mechanism` and depends on the `Utility` interface, which is implemented by `UtilityImpl`

**Note:** Now the lower-level code has dependencies on the higher-level abstractions! 
Hence "dependency inversion."

## SOLID in Practice

How important is it to follow *all* these properties *all* the time?

***Donnie's suggestions:***
- Always follow LSP and ISP—they are important for correctness
- Follow the other properties when it's convenient and simple to do so
- Be prepared to refactor your code when you identify areas more likely to change or require extension

Follow the **Rule of Three** (*Refactoring*, Martin Fowler): 

> *"Here’s a guideline Don Roberts gave me: The first time you do something, you just do it.  The second time you do something similar, you wince at the duplication, but you do the duplicate thing anyway. The third time you do something similar, you refactor. Or, for those who like baseball: Three strikes, then you refactor."*