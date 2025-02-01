# High-Level Patterns

## Testing Terminology

**Unit test** = a test that quickly verifies a single unit of code in an isolated manner
- *Positive:* verify a success scenario
- *Negative:* verify a failure scenario

**Integration test** = a test that exercise multiple units of code that interact with each other or individual units of code that interact with external dependencies

**End-to-end test** = an integration test that includes *all* internal and external dependencies of the software

**Smoke test** = a very fast set of tests that only covers the most critical functionality of the project

## The Testing Pyramid

1. Small number of E2E tests
2. Some more integration tests
3. Many unit tests

From 3 to 1: 
- Closer emulation of user
- Better protection against regressions
- Increased complexity
- Slower performance
- Increased cost of setup
- Reduction of isolation
- Difficulty of diagnosis

Generally, the more code exercised in a given test, the
- better it is at finding regressions,
- harder it is to find the cause of a fail,
- slower it runs, and
- more setup is required

## Tests and Dependencies

**System Under Test (SUT)** = unit of code being tested by a UT

- A *shared dependency* may be used by multiple tests
- A *private dependency* is only instantiated and used by one test
- An *out-of-process dependency* exists outside the test program's process (e.g., database servers, filesystems, etc.)
- *Immutable dependencies* (or *value objects*) cannot by changed by the test code
- *Mutable dependencies* (or *collaborators*) can have their state altered by tests
- *Volatile dependencies* require setup or tear-down and/or exhibit nondeterministic behavior

## Unit Tests: isolation

What do we mean by, ". . . in an isolated manner"? Two schools of thought:

1. **Classical** (or **Detroit/Chicago**) unit testing:
    - Unit *tests* must be isolated from each other
    - Only private dependencies are allowed, no shared 
    - collaborators are allowed
    - (Out-of-process dependencies are excluded because they are slow)

2. **Mockist** (of **London**) unit testing:
    - *Units* must be isolated from each other
    - Besides the SUT, only value objects are allowed, no collaborators
    - (Out-of-process dependencies are excluded because they are slow)

The classical style of testing focuses primarily on verifying *observable state* whereas the mockist style of testing focuses primarily on verifying *behaviors*.

Which is better? Depends on the problem. (Example: Mocks are very useful for verifying subsystems whose observable behavior must follow specific patters, e.g. caches)

## Test Doubles

**Test doubles** = "pretend objects" used in place of real objects in tests

- *Dummy* objects have no implementation; they are passed around but never used
- *Fake* objects have working implementations, but they are not suitable for production
- *Stubs* provide canned answers to calls during a test
- *Spies* are stubs that also record details about how they were called
- *Mocks* are pre-programmed with expectations as to how they will be used by the SUT
    
