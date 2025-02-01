# Quality Assurance

QA is the process of ensuring that the software we create is of high quality
- Not just correctness!
- Usability, modifiability, performance, . . .

Must engage in QA *from the start!*
- The longer a defect goes undetected, the more costly it is to fix

**Automated software testing:**
- Run tests after changing code to make sure program is still correct
- Can be run on a periodic basis, e.g., when new code is committed

## Costs of Fixing Bugs

> *"The longer a bug exists, the more expensive it is to fix"*

Why: 
1. You don't want clients running into your bugs!
2. Developer will forget the details of old code

    **Eagleson's Law:** 
    > *"Any code of your own that you haven't looked at for six or more months (more like 3 weeks) might as well have been written by someone else"*
3. Other code may start to depend on buggy behavior

    **Hyrum's Law:** 
    > *"With a sufficient number of users of an API, it does not matter what you promise in the contract:  all observable behaviors of your system will be depended on by somebody."*

    AKA every change breaks someone's workflow.

## Regressions

Software development is *iterative!* But that also means it's easy to break stuff when adding new features (**regression**).

- *Regression testing* focuses on verifying that implemented features continue to work

## Testing Goals

Ideally, testing is **automated**, **reasonably complete**, and **fast**

- Gives developers *confidence to make improvements*
- Facilitates *refactoring*

*Donnie tip:* If you're ever afraid to change something in your code, ask yourself if it's because you don't have enough tests.

**Test failures should be easy to diagnose!**
- Name tests to clearly indicate their purpose
- Use clear/concise docstrings (printed when test fails)
- Follow the Arrange-Act-Assert pattern
- Each test exercises *one* thing

Ideally, tests should be written to maximize **robustness** in the face of code changes.

> *"Code is a liability, not an asset. What code does for you is an asset."*

More code isn't necessarily better! This is true for tests as well.

**The most robust tests focus on *user-observable* state/behavior**

## Measuring Test Completeness

- **Code coverage** = What percentage of the program's lines of code were executed during a test suite? It's as easy as `pip install coverage` in Python.

    **(!)** Donnie warning: High CC doesn't necessarily mean you have *good* tests! But low CC does indicate where new tests need to be written

- **Branch coverage** = What percentage of a program's branches were executed during a test suite?

- **Cyclomatic complexity** = Number of linearly independent paths through the code

- Code coverage measurements are not always cheap, and they may interfere with other kinds of tests (like performance or concurrency tests).

- Setting a specific test-coverage goal is viewed as an *anti-pattern* in the software industry. 

    > *"When a measure becomes a target, it ceases to be a good measure."* —Marilyn Strathern

- Tests concentrating on **key functionality** will have greater long-term value that test of simple, peripheral function, glue code, etc.

- Tests should focus on the **hard stuff**. Bugs are not evenly distributed; they show up in the most complex, critical areas.

## Defect Detection Rates

Even though tests are great, they don't catch everything.
It's best to have a *diverse set of techniques* to detect defects in the code (modeling/prototyping, collaborative code reviews, etc.).

## Why Automated Testing

1. Gives visibility into project's code quality
2. Forces developers to think about code structure/interface as they are writing

## A Culture of Testing

Projects must develop and maintain a culture of testing:
- Advocate within your team
- Treat test code as important as project code
- Always fix all test failures
- Use test coverage tools to identify under-tested code