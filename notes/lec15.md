# Version Control / Git 201: Trunk-Based Workflows—Git Best Practices

## Feature Branches

Feature branches isolate devs from each other.
It's easy to get merge conflicts!

Even if you merge from `main` into your feature branch regularly, in workflows like Git Flow, other dev's features won't appear in `main` until they are *entirely completed*.

Main Point:
> *Merge-conflict pain increases with the **number of live feature branches** and the **length of time that feature branches exist**.*

To minimize pain:

- If you know that two feature branches involve the same code, can simply merge back and forth between them regularly.

- *Keep all branches as short-lived as possible!*

    - The Atlassian internal dev model encourages creating branch per "task"

## Continuous Integration (CI)

The meaning of CI has changed over the years.

**Today:** CI is the practice of automatically running tests on the main development branch of a repo after every commit, *regardless of the branching model used*.

**Original definition:** CI is the practice of merging the work of *all* devs into a single repo (i.e. branch) on a daily basis and verifying the quality by automatically running tests on the repo (Grady Booch, early 1990s).

Donnie likes this old definition because it *minimizes merge conflicts*.
But how do you deal with features that take longer to implement?

## Trunk-Based Development

*Idea:* Use **feature toggles** or **feature flags** (see https://martinfowler.com/bliki/FeatureFlag.html) to guard new, incomplete features from being used at build/run time.

*Consequence:* A feature's code may be included in multiple releases before it is finally turned on for end-customer use.

- *Example:* Chrome/Firefox have experimental features that you can turn on/off and submit bug reports on

The trunk of the repo is automatically tested on a regular basis, typically with two configurations: 

1. All "official release" feature toggles turned on; everything else off

2. All feature toggles are turned on

Once a feature is stable and widely used, its feature toggle is removed.

This strategy is called [Trunk-Based Development](https://trunkbaseddevelopment.com/).
It requires a high level of discipline from devs.

- Very easy to break the project for everyone

- Build and test automation is very important

- Implementing comprehensive tests is extremely important

The up-side: **merge conflicts are very small and easy to resolve!**

Google, Meta, and Amazon us trunk-based development and feature toggles for their products. 
Microsoft also uses something like trunk-based development on many large products.

Increasingly, large companies have been moving towards keeping all code for all products in a single **monorepo** ("monolithic repository").

- *Donnie Recommendation:* Watch [this video](https://www.youtube.com/watch?v=W71BTkUbdqE)!

- Excellent for code reuse, refactoring, build/release management, code reviews, etc.

- Requires dev discipline to keep everything clean and well-organized

### Other Trunk-Based References

- [How We Use Git at Microsoft](https://learn.microsoft.com/en-us/devops/develop/git/what-is-git)

- [Scaling Mercurial at Facebook](https://engineering.fb.com/2014/01/07/core-infra/scaling-mercurial-at-facebook/)

## Repository Workflow for Research/OSS

**Should `main` be the integration branch for your project repo?**

Open-source projects with junior contributors likely want to consider keeping `main` as a "release-quality" branch, a la Git Flow. Reasons:

1. Expectations of code on `main`

    - Researchers and junior contributors may not be savvy enough with Git to examine a repo's tags/branches before starting usage or development

2. Maintain project quality and stability

    - Most researchers and junior contributors will likely contribute code with bugs, maintainability issues, and other code smells

    - Encouraging the use of feature branches allows issues to be addressed before introducing new code into `main`

## Repository Management Best Practices

### Working Copies

- Keep your working copy up to date with work done by others in the repo, particularly if their work affects you

    - Pull updates regularly

    - If doing feature-branch based dev, merge from trunk regularly

- Don't update your local working copy if you know others have broken the software!

    - Communicate with your team to be aware of who is working on what and when dev efforts may overlap/conflict

### Commits

- Always commit when you complete one "unit of work" 

- Write useful commit logs that explain the reasons for your changes (use the 50/72 format)

- If you have a demo-worthy version of your project, tag it!

- As much as possible, keep each commit as small and focused as possible while also being complete

### Tagging

- Come up with a tag naming convention for your project and follow it

- When a tag is pushed to remote, treat it as "set in stone"

### Branching

- Devise a strategy for branching up front!

- Use a naming convention and follow it

- Delete branches when you're done with them

### Feature Branching

- Risky, but works really well for some

    - Nasty merge conflicts are a constant risk

- Feature branches should last a very short time (1 to 3 days max)

    - Use feature toggles to guard new code

- Avoid divergence between `main` and feature branches

    - Keep in mind the original CI definition

### Release Branching

- Do it!

- Since major releases are backwards-incompatible, it makes sense to branch per major release version

    - Tag minor/point releases on major-release branch

- Primary issue: bugfixes or hotfixes on releases

    - Need to make sure release bugfixes make it back into `main`

    - Fix 1: make bugfixes on `main` and cherry-pick them into release branch (main issue: `main` may have already diverged too much from the release branch)

    - Fix 2: make bugfixes directly on the release branch (just don't forget to merge the bugfix into `main`!)

### Test Automation

- Too costly (and not that helpful) to do on all branches

- Automated tests should run on the integration branch at least once a day, more if possible

- Release branches should run automated tests on every commit

### Rebasing

- Always follow the Golden Rule of Rebasing: *Never use rebase on a public branch*!

- Always rebase when pulling from a remote repo: `git config --global pull.rebase true`