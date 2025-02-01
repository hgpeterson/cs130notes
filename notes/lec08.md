# Software Testing: Implementation Patterns

## "Good" Unit Tests

Protection against regressions
- Focus unit tests on **important** and **complex** features
- Testing "trivial" code may find bugs, but those bugs would likely be obvious anyways

Resistance to refactoring
- A refactor should not change the visible behavior of the program
    - Don't want *false positives* where system is correct but tests fail
    - While a *deficient* test suite will prevent developers from making improvements, so will a *fragile* one!
- Tests are resistant to refactoring if they only examine state and behavior observable by the client, not implementation details
    - If you do need to test some complicated helper function, maybe that means you need to break it down into smaller pieces

Fast feedback
- Faster tests are more likely to be run by developers

Maintainability
- Test code must be maintained just like project code!
- If tests are easy to understand, and easy to run, maintenance costs will be minimized

## "Good" Integration Tests

Same ideas as the UTs, but with more code, dependencies, and complexity.

## Protection Against Regressions

**Black-box testing** = exercise system without considering any internal implementation details
- Generally written by people other than original developers
- Good for making sure code actually satisfies the specifications

**White-box testing** = exercises system using knowledge of implementation details
- Generally written by original developers
- Good for getting a high code coverage

## Test Construction

### Basis Path Testing

**Basis path testing** will give you a sense of how many tests are necessary to reach full branch coverage. This is a form of white-box testing.

Given a unit of code you intend to test:
- Start with 1 for the straight path through the code
- Add 1 for each of: *if*, *while*, *repeat*, *for*, *and*, *or* (or equivalents)
- Add 1 for each case in a switch statement, plus 1 if there is no default case

*Donnie tip:* If a piece of your code yields a very large number, maybe it should be broken down.

### Boundary Values

**Boundary value analysis** focuses on tests that exercise values from the  full range of possible inputs. Can be either white- or black-box depending on values

Example: functions that take numeric inputs
- A value from a range of valid values
- A value just below the maximum value
- The maximum value
- A value above the maximum value

Example: functions that operate on a list
- An empty list
- A list with one value
- A list with multiple values

Very useful for finding **off-by-one** errors!

Illustrates an important guideline for tests:

> *"If two tests will flush out the exact same error in the code, get rid of one of them!"*

### Brute-Force Testing

Don't underestimate the value of **brute-force testing**! 
Exercising all code paths by enumerating all possible inputs can be a very straightforward approach to achieve full test coverage.

- Should be complemented with unit tests that exercise simple scenarios, boundary values, error scenarios, etc. so you can actually find basic issues quickly

**Fuzz testing** = Making sure a system behaves soundly for all kinds of random inputs.

### White-Box vs Black-Box

**Goal**: Generally want to be biased towards *black-box* testing.

Use white-box testing to:
- Evaluate if your test suite is complete or not
- Evaluate if your implementation is unnecessarily complex

If your implementation is sensitive to values not identified in the spec:
- The spec may be incomplete. . .
- . . . or, your implementation may be overly complicated.

## Implementation Pattern

Typical pattern: setup, exercise, verify, teardown.
Often abbreviated **AAA** for:
1. Arrange
2. Act
3. Assert

Maximizes maintainability and readability of test code.

Having multiple Act/Assert steps in a single test is an anti-pattern.
- This is a sign that you really should have multiple unit tests
- Sometimes this is a good idea if the Arrange step is very expensive (e.g., for an Integration Test)

## The System Under Test

|                  | Few Collaborators | Many Collaborators |
|------------------|-------------------|--------------------|
| **Complex**      | UNIT TEST         | REFACTOR           |
| **Simple**       | DON'T TEST        | INTEGRATION TEST   |

## The Humble Object Pattern

Frequently, units that are difficult to test have multiple components internally.
- E.g., a big piece of code with domain logic and a hard-to-test dependency.

Solution is the **humble object pattern**.
- Factor out the domain logic
- Create a humble object that coordinates interaction between domain logic and hard-to-test dependency
- Hopefully the humble object is so simple you don't have to test it

