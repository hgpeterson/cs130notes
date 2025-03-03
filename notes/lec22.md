# Software Architectural Tactics

## Quality Attributes

Quality requirements aren't always clearly and concretely specified.
Recall *SMART:* Quality requirements should be Specific, Measurable, Attainable, Relevant, and Time-sensitive.

Often, QAs have overlapping scopes and impacts. 
Example: A system may encounter denial-of-service attacks.
What QAs are relevant?
- Availability, Performance, Security, Usability?
- Each QA focuses on different aspects of response to DOS attacks
- For each QA, terminology varies:
    - Availability considers "system failures," recovery, MTTF and MTTR measures
    - Performance considers "events," latency, throughput, etc.
    - Security considers "attacks" and how they are handled
    - Usability considers "user input," throttling, etc.

**Development** and/or **Runtime** QA:
- Modifiability, Testability, Debuggability, Deployment

**In-Operation** QA:
- Availability, Performance, Scalability, Usability, Safety

"System Under Development" Example: **Web Browsers**
- Modifiability: plugin support for 3rd-party devs
- Deployability: can check if user is running latest version, upgrade when necessary
- Testability/debuggability: often have "developer consoles" and logging

A more formal way to specify QA through **scenarios**:
1. **Stimulus**: an event, incoming request, the completion of a programming task, a fault, etc.
2. **Stimulus source**: who or what initiated the stimulus (user, system, device failure, programmer, bug, etc.)
3. **Response**: system's response to the stimulus
4. **Response measure**: quantifies a satisfactory response (remember SMART)
5. **Environment**: where the scenario takes place (normal/degraded state, typical/heavy load, release state)
6. **Artifact**: portion of the system under consideration

## Tactics

Architectural patterns are generalized and include some design choices.
Often, many other techniques can be applied in a project to achieve various QR—these are called **architectural tactics**.

When evaluating a framework:
- Have a sense of what QR are relevant to your project
- Examine frameworks to see what tactics they support

You can also incorporate specific tactics into a design yourself.
In either case, **research what others have tried and whether they ran into difficulties!**

Let's explore some example QAs and tactics.

## Availability

**Availability** is a quality of software that is ready to perform its task at any given time.
- Includes reliability and recoverability
- Related to security (needs to be resilient against, e.g., DOS attacks)

In terms of the **scenario** terminology, the *stimulus* in this case is a *fault*.
Possible response measures:
- Time in which system must be available
- Availability percentage (e.g., 99.999% or faults only about 5 mins per year)
- Time to detect

### Tactics

- Detect faults
    - Ping/Echo, Monitor, Heartbeat: all monitor health of a server by listening for an expected response
    - Timestamp, Sanity Checking, Condition Monitoring, and Voting: all examine program outputs for valid state
    - Self-test: can be employed when a component includes the capacity to run various diagnostics on itself
- Recover from faults
    - Preparation and Repair
        - Maintain redundant systems ("hot" spares mirror the system, "warm" spares are periodically updated, "cold" spares need building to get started)
        - Rollback and Software upgrade: record "known good" system state to use when recovery occurs
        - Retry: when failures may be transient, try again later 
        - Ignore faulty behavior, degradation, reconfiguration: isolate failed components and run with reduced capabilities until recovery can be completed
    - Reintroduction
        - Shadow, State Resynchronization: focus on resyncing the failed server with current state
        - Non-stop forwarding: used when a system is divided into supervisory/control functionality and operational functionality
- Prevent faults
    - Removal from Service: temporarily remove and/or restart software components to eliminate latent fault conditions
    - Transactions: actively rollback system to known good state
    - Predictive model: in conjunction with monitoring, detect scenarios when the system is likely to fail and proactively respond
    - Increase Competence Set: design software to handle more faulty conditions

## Testability

**Testability** focuses on how easy or difficult it is to get a software system to *reveal its faults*.
Must be able to easily control a program's inputs, outputs, and internal state

In terms of the *scenario* terminology, the stimulus source may be unit/integration/system testers. 
Some possible response measures:
- Effort required to find a fault
- Effort required to achieve a given percentage of state space coverage
- Probability of a fault being revealed by test
- Time to perform tests

### Tactics

- Control and Observe System State
    - Specialized Interfaces: provide access to internal state, state mutation, and other facilities that make it easier to write tests
    - Record/Playback: makes it much easier to validate whole-system behavior by recording sequences of operations and their results
        - Operations can be played back (or a scenario can be re-run) and state can be examined to see if it matches verified output
        - Failures can be recorded, making them easier to debug
        - *Donnie tip:* This is great for software that runs **simulations**!
    - Localize State Storage: state values should be stored in a single place
        - They will be easier to access when you are writing tests against the code
    - Abstract Data Sources: allow programs to receive inputs from alternate sources, such as a test harness
    - Executable Assertions: an essential mechanism for building testability into your code
        - Your program can check for invalid inputs/outputs/state as it runs and will stop automatically if an assertion fails
        - Virtually all programming languages support assertions and the ability to disable them in production
- Limit Complexity
    - Limit Structural Complexity: maximize ability for components to be exercised and tested in isolation of the entire program
    - Limit Nondeterminism: consistent and predictable program behavior greatly simplifies testing

## Usability

**Usability** is focused on how easy it is for a user to accomplish a desired task and what kind of support the system provides for the user.

In *scenario* terms, the *stimulus* is the end user learning to use the system.
Response measures may be:
- Time to complete task
- Number of errors
- Number of tasks accomplished
- User satisfaction

### Tactics

- Support User Initiative
    - Cancel
    - Undo
    - Pause/Resume
    - Aggregate: allow user to perform same operation on many items at onces
- Support System Initiative
    - Task Model: allows the system to know the context of a user operation so that it can facilitate the user's action
    - User Model: allows the system to model or gauge the user's knowledge or behavioral characteristics so that it can adapt to the user's needs
    - System Model: allows the system to accurately estimate the cost of significant operations so that the user can make better decisions

## Other QAs

If you have a QA you aren't certain how to achieve:
1. Work wit stakeholders to develop specific scenarios for the new QA
2. Review existing approaches
3. Identify parameters the new QA is sensitive to
4. Talk to domain experts about the new QA
5. Enumerate a set of tactics for the new QA
