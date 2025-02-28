# Software Architectural Patterns

**Key result from last time:** software architecture is focused mre on achieving the non-functional attributes of a software system (AKA quality attributes like robustness, scalability, performance, portability, etc.).

Certain kinds of software development problems are recurring, leading to common **architectural patterns** used to solve them.
They typically describe:
- A context: the recurring situation
- A problem: issues that arise from the context
- A solution: a successful architectural resolution to the problem

The solution typically specifies:
- Structural constraints on the system 
- QAs that benefit—or are hindered by—the approach
- Relationships between modules
- Functional components of the system and how they interact
- Allocation/placement of modules and components

Some example architectures we will consider today:
- Layered
- Multitier
- Model-View-Controller (MVC)

Others you can look into:
- Publish-Subscribe
- Pipe-and-Folder (based on the UNIX model; good for data processing)
- Map-Reduce (good for processing large datasets)

*Donnie tip:* Knowing more about common software architectures can help you recognize when to use them!

## Layered Architecture

**Layering** is a structural pattern for how to organize code into modules.
Each layer is a cohesive set of services, exposed through a public API.

**Problem being solved:** Support portability, modifiability, and reuse by dividing software into layers.
Allows for parallel development of layers.

**Visualization:** A stack of boxes read from the top down.

*Must* specify:
- What layers exist in the system
- The purpose of each layer
- What software components are allocated to each layer
- Which layers may be accessed by each layer
    - Typically, each layer may only access the layer *immediately below it*
    - **Layer bridging**, where a layer may access nonadjacent lower layers, is sometimes allowed. 
    This may adversely affect portability and modifiability attributes, however.
    - ***Never* let a lower layer access a higher layer!**

**Note**: Each layer should be modifiable or replaceable without affecting any other layers.

Layers can also have complex internal structures (called **segmented layered architecture**).

**Limitations:** 
- More layers increases cohesion of each layer but also reduces performance
- Tends to increase complexity of system design, since each layer must be carefully designed to support the layer(s) above it

## Multitier Architecture

**Multitier** (or **n-tier**) architectures are very useful for building client-server systems.
For example, in our online auction website from last time, we had a **presentation layer**, a **business layer**, and a **data access layer**.

Multitier is very similar to layered, with two main differences:
1. Multitier architectures are used specifically for building client-server systems, while layered architectures can be used to build anything
2. Tiers differ from layers in that they have a physical run-time structuring aspect.
Different tiers are often deployed onto separate physical systems to improve performance, robustness, etc.

More detailed online auction website tier structure:
- Client "tier"
    - UI HTML scripting
- Presentation tier
    - Authentication filter
    - Web-UI controller
    - Auction notifier
- Logic tier
    - User profile
    - Payments
    - Auctions
    - Data caching
- Persistence tier
    - Domain objects
    - Database server

Tiers usually interact with each other using a variety of protocols (e.g., HTTPS, JDBC, REST calls, other RMI protocols, IPC).
Very complex systems may include even more tiers!

Multitier architectures are **most useful** when:
- Different tiers have significantly different platform requirements
    - e.g. presentation tier may require large CPU/memory resources while database tier requires fast storage access
- The overall system has demanding performance/scalability/reliability requirements
    - Multiple instances of a given tier can be deployed to increase performance by scaling horizontally
- Some tiers need to be run in a highly secure environment
    - e.g. payment processing, personal data storage

**Limitations:**
- Complex and challenging to implement
- System deployment becomes significantly more complex
- Debuggability of the system is reduced unless this is specifically planned for

## Model-View-Controller Architecture

**Model-View-Controller (MVC)** is often used when user interfaces are involved.

**Problem being solved:** 
- *Modifiability:* separate concerns between what is displayed, how it is displayed, and the behavior of the UI
- *Modifiability:* these different aspects tend to change with different frequencies, with display being changed the most frequently
- *Usability*: users frequently benefit from multiple views of the same underlying information

Components:
- **Model:** data to be displayed
    - Encapsulates application state
    - Enforces basic business logic
    - Provides operations to query model state
- **View:** user interface for rendering model state
    - Queries the model for data to display
    - **Never modifies the model directly**
    - Must be informed when model's state has changed
- **Controller:** dives the UI behavior
    - Based on user interactions, makes changes to the model and/or view
    - Implements validation of user input

There are many variations on MVC. For example, **hierarchical MVC** is very common (e.g., iOS).

**Benefits:**
- Strong *cohesion* within each component
- Loose coupling between components
- Generally very easy to modify view and/or controller in minor ways

**Limitations:**
- Must maintain *consistency* across three different components
    - Example: When the UI must expose a new value, model must expose access to the value, new state-change notifications for value, view must be updated to display value, controller must properly manipulate the value. . .
- For very simple user interfaces, MVC is often overkill
- MVC may not work very well in UI frameworks not designed for it (unlikely)