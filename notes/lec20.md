# Software Architecture

**Software architecture** = the overall structure of the software system. 
The components, how functionality maps onto them, and how they communicate with each other.

**Software design** = similar idea, but tends to refer to lower-level ideas (e.g., subsystems).

> *"Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change."* —Grady Booch

> *"Architecture is the decisions you wish you could get right early in a project but that you are not necessarily more likely to right than any other."* —Ralph Johnson

> *"Architecture is about the important stuff. Whatever it is."* —Martin Fowler

## Example: Online Auction Website

As an example, let's think through building a website to ost online auctions of items at a college.

### Approaches

1. Monolithic 
    - Implement website as a collection of PHP pages, each of which includes the business logic, DB access/SQL query code, and display text, all in one place
2. Layered
    - Divide implementation into three layers: presentation, business logic, and persistence
    - Each layer is implemented in its own set of files
    - Each layer provides a specific API to the layer above it
    - Each layer may only interact with the layer immediately below it

**Which approach is better and why?**
- First approach is faster to implement and could be simpler for a small-scale site
- Second approach is more organized, follows GRASP, etc.

*Depends on the scenario!* 
Maybe #1 is best for a first prototype to show investors.

Suppose **popularity grows** and now we need to update the website to:
- Use language based on client's locale
- Add new auction type with movable ending time
- Move from sqlite to a proper database like MySQL/Postgres

**Approach 2 will be much easier to make these changes with!** 
It's more flexible, changes will be isolated, and it's easier to write tests that will verify each layer

Within approach 2, we can make different choices:

- 2a: Run all layers within a single web server
    - Apache HTTP Server on NGINX using PHP support
    - Easy for layers to communicate; they just call each other's APIs and return objects within the same process address space
- 2b: Run each layer on its own server(s)
    - Layers have to communicate somehow, e.g. with remote method invocation (RMI), web-API calls (SOAP, REST, ???), etc.

**Which approach is better and why?**
- 2a Pros:
    - Easier to implement 
    - Less complexity in the communication between layers
    - Less complexity managing authentication/authorization across layers
    - Easier to deploy
    - Easier to debug
- 2a Cons:
    - May not scale to the required number of concurrent users
        - Increased latency/response time for server requests
        - Bottlenecks on the server, e.g. CPU, memory overhead, network bandwidth
    - May not be able to provide desired reliability guarantees
        - A single server is a single point of failure
- 2b Pros:
    - Much easier to scale
        - Scale up number of servers for each layer type depending on performance
        - Distribute servers around the world to reduce network latency overhead
    - Better reliability (as long as failover is properly engineered)
    - Easier to implement A/B testing for UI changes, new features
- 2b Cons: 
    - Authentication/authorization
    - Persistence/DB tier is notoriously difficult to move to multi-server
    - Debugging becomes extremely difficult
    - Deployment becomes complicated

Keep the **CAP Theorem** in mind:
> *"You can only pick two of (C)onsistency, (A)vailability, and (P)artition tolerance."*

## Architecture and Requirements

*Given enough time and effort, can we implement all features of our website with all of these approaches (1, 2a, and 2b)?*

*YES!*

**Software architecture** has little to do with realizing the functional requirements of a software system—it is all about **achieving non-functional (e.g., quality) requirements of a software system.**
- Good software architectures **maximize our ability to achieve the required quality attributes** for a specific project
- They do this with a **minimum amount of effort**
- Most critical quality attribute: ***modifiability***