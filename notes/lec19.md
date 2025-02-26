# Software Diagramming Techniques

Diagrams can be helpful for communicating ideas.
- Useful during requirements-gathering discussions
- Need to have a **standard format** so everyone knows what you're talking about

## UML

**Unified Modeling Language (UML)** documents both the **static structure** (e.g., stuff sitting on servers) and the **dynamic behavior** (e.g., how components interact) of software systems.
Two main types of diagrams: 
1. Class diagrams for static structure
2. Sequence diagrams for dynamic behavior

### Class Diagrams

**Goal:** describe the classes and their attributes/responsibilities/relationships in the program.

- **Domain models** capture the kinds of data the program must work with along with the relationships between them (independent of persistence questions).

- **Database schemas** capture specific types (and associations between them) that must be stored in a database.

In both of these diagrams, the *"things"* are called **entities** and the associations between them all called **relationships**.

#### Classes
- **Classes** are modeled with a rectangle containing the name of the class
    - Can also list the attributes and methods in sub-sections of the rectangle
    - **Abstract classes** are have *italicized* names (and attributes/methods)
- Can specify both *type* and *visibility* of **class members** with the conventions:
    - "+" = public
    - "-" = private
    - "#" = protected
    - "~" = package

#### Relationships

- **Association** is the simplest kind of relationship 
    
    Example: Person——Company

    - Modeled with a solid line
    - Can label the line with specifications
    - Numbers for how many objects can be connected through the association ("*" for "unlimited")

- **Aggregation** is a "parts of a whole" type of relationship

    Example: PrinterUser♦——3DPrinter

    - Modeled by a diamond on the "whole" side of the association
    - Describes "has a" relationship between entities
    - Use a hollow diamond if the two classes can exist independently; use a solid diamond if one should be removed if the other is deleted.

- **Generalization** is when a specialized class *inherits* from another more general class

    Example: Teacher️——▶Person

    - Modeled by a solid line with a hollow arrow


- **Interfaces** only specify operations

    Example: ArrayList- - -▶«interface» List

    - Modeled with «guillemets» 
    - Use hollow-head arrow with dotted line to indicate implementation of interface

- Can specify **navigation constraints**

    Example: GameLobby——>Player

    - Bidirectional associations (no arrows) allow easy traversal in either direction
    - Unidirectional associations can only be traversed easily in one direction

- **Dependencies** indicate that a change in the target is likely to require changes in the source

    Example: ArrayList- - ->IndexOutOfBoundsException

    - Indicated with an open-headed arrow and dashed line
    - Unidirectional


### Sequence Diagrams

**Goal:** For a given usage scenario, identify the participants involved and the interactions between the mover time.

Notation:
- Participants (classes, users, etc.) have a **lifeline** and interact with each other via **messages** of various kinds with time progressing downward.
- "Start operation" = arrow with solid line
- "End operation" = arrow with dashed line
- Time spent within a given participant is called an **execution**
- Initiator of operation appears to the left of the receiver
-Can represent repeated interaction with "loop" block, object creation/destruction, and more. 

Easily becomes unwieldy for large, complex interactions.

## Flowcharts

Much simpler than UML, but gets the job done.

**Goal:** Sketch out behavior of a data processing pipeline or user interaction.

- **Entry points** are drawn with filled-in circle
- **Exit points** are drawn with filled-in circle inside of an open circle 
- **Processing steps** are drawn as a rectangle
    - Lines between steps are called **flowlines**
- **Decisions** are drawn as a diamond.

**Swimlane diagrams** are flowcharts where steps are subdivided into specific roles, with each role having its own "lane."
- Help find bottlenecks and key actors

## Agile Diagramming

Stay agile!
If you use UML diagrams, don't be overly fussy about representing everything precisely.
Try to be light-weight!

[Example](http://agilemodeling.com/artifacts/sequenceDiagram.htm) from Scott Ambler: "Enroll in a university"


