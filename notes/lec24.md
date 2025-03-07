# Donnie's Favorite Design Patterns

Donnie's favorite book: *Design Patterns:
Elements of Reusable Object-Oriented Software*, Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (1994).

**Design patterns** are common solutions to problems that have repeatedly arisen in software development efforts.
These patterns are given names so that devs can communicate more effectively. 
**The more patterns you know, the easier it will be to find the right solution for a problem!**

The *"Gang of Four"* design patterns fall into three categories:
1. Creational patterns
2. Structural patterns
3. Behavioral patterns

This aligns with the focus of the GRASP principles/patterns (where to place knowing/doing responsibilities and object-creation responsibilities).

## The Iterator Pattern

There are several ways to implement collections, each with its own strength and weaknesses:

1. Array-backed lists
    - Constant-time indexing of a specific element ✅
    - Easy forward/backward traversal ✅
    - Linear-time prepend (need to move values over to make space) ❌
    - No extra space required for each element ✅
2. Singly linked lists
    - Linear-time indexing of a specific element ❌
    - Forward-only traversal ❌
    - Constant-time prepend ✅
    - Each element requires extra space ❌
3. Doubly linked lists
    - Similar to singly linked lists, except forward *and* backward traversal (✅), and each element requires two pointers instead of one (❌)

**How do we code algorithms *generically* against different kinds of collections?** *Iterators!*

The **Iterator** design pattern solves the problem of handling different kinds of collections.
It is ubiquitous in nearly all languages.

The idea is to, rather than having code that traverses collections to know internal implementation details, collections provide an *iterators* that implement and encapsulate collection-specific traversal of their elements.
- All iterators implement a simple, well-defined << interface >>

Algorithms then just interact with the abstract Iterator interface.
This is an example of a **Factory Method** pattern.

**Problem:** How do we implement `reverse()` and `sort()` algorithms for collections that don't support backward traversal?
- Many languages provide a more sophisticated hierarchy of iterators for collections to implements
    - `SinglyLinkedList` might provide a `WritableIterator`
    - `DoublyLinkedList` might provide a `BidirectionalIterator`
    - `ArrayList` might provide a `RandomAccessIterator`
- Algorithms can provide optimized implementations for their preferred kinds of iterators, as well as simple fallback versions when a collection can't provide the optimal kind of iterator

## The Visitor Pattern

The **Visitor** design pattern is basically the same as the Iterator pattern but for *hierarchies* of objects.
Specifically, it works with trees of objects where nodes may be of different types and may have different numbers of children

**Example:** Formula in a spreadsheet
- Want evaluate formula based on parse tree
- May need to identify dependencies on other cells
- Will also need to update cell-references to rename sheets or move cells
- If we define an `Expression` class and demand all types implement this, things will be too tightly coupled
    - Adding new operation would require updates on all classes in the hierarchy
- Idea: Factor out algorithms into separate classes that implement an `ExpressionVisitor` interface
    - Interface has a method for each kind of element in the expression hierarchy
    - To simplify visitor implementations, can provide an implementation of this interface with no-op methods
    - Each subclass of `Expression` must implement the `accept()` method to call the visitor, e.g.
    ```
    class AddExpr(Expression):
        ...
        def accept(self, visitor):
            self.left.accept(visitor)
            self.right.accept(visitor)
            visitor.visitAddExpr(self)

    class Number(Expression):
        ...
        def accept(self, visitor):
            visitor.visitNumber(self)
    ```
    - In Julia, this is pretty easy using multiple dispatch
    - The `Lark` parser leverages Python's dynamic method lookup `getattr(object, name)`. A visitor implementation simply provides methods named after the grammar's token names (no need for an explicit `ExpressionVisitor` interface)

**Drawback of the Visitor pattern:** New elements in node hierarchy are likely to require changes to existing visitor implementations.

## The Proxy Pattern

In many situations, we want a placeholder for an object, such as when it is:
- Expensive to create
- Not on the local machine
- Etc.

A **Proxy** is a placeholder or surrogate to another object that presents the same interface as what it represents.
The object and its proxy are built around well-defined interfaces.

**Example:** Web browser
- Images and other kinds of figures can initially be represented with proxy objects
- Allows page to be laid out before image is loaded
- When the image must be drawn, the proxy can load it "just in time"

**Example:** Smart pointers
- Smart pointers wrap "naked pointers" to heap-allocated objects
- They handle deallocation of objects in OO languages with manual memory management (example: `std::shared_ptr<T>` in C++)

## The Adapter Pattern

The **Adapter** pattern is like the Proxy pattern, but the adapter doesn't provide the same interface as the wrapped object.
Instead the adapter provides a different programmatic interface to facilitate use with a different API.

**Example:** Sorting regions of a sheet
- Build an adapter class that wraps a row of spreadsheet data so it can be sorted as a unit
- Use Python's built-in sorting implementation against regions of your spreadsheet
    - Without the adapter class, you would've had to implement sorting yourself!

## The Singleton Pattern

Sometimes there must be exactly one instance of a given class, and it must be easily accessible from many parts of the program.
This is the **Singleton** design pattern, and it should be used *cautiously!*

**Common issue:** If not implemented correctly, the Singleton pattern can create big headaches when testing.
- Do I need to provide a different version of the singleton instance for testing? If so, how?
- How do I provide another implementation (e.g., a subclass) of the singleton when the common implementation isn't appropriate 

Singletons are often eliminated from programs by applying the dependency injection pattern.