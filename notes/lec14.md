# Version Control / Git 201: Feature Branch Workflows

Today we'll discuss patterns for using Git to manage large source-code repos in a more structured, coherent manner.
Just like with agile vs. waterfall, there are many approaches.
*Choose a strategy that matches your project's needs!*

## Repository Management

### Pains

1. **Merge conflicts:** When local copy of code has diverged significantly from the "official version" and must be re-integrated 

2. **Checking out broken code:** When someone else checks in broken code, you check it out, and you don't know how to fix it

    - This includes **regressions**, features that previously worked but then became broken later

### Goals

1. Keep code quality high

2. In cases of risky dev tasks: minimize impact on other devs/code quality

3. Provide *very* stable environment for preparing releases

## Code Quality

What do we mean by **"Code Quality"**?

- Completed features keep working (no regressions!)

- New code landing in the repo is well designed, bug-free, well documented. Each commit should *improve* the overall health of the codebase!

In our Git 101 series, we learned about *feature branches* as a way to maintain high code quality on the `main` branch.

## Release Management

How do we **"provide a *very* stable environment for preparing releases"**?

Multiple phases of software project:

1. Alpha software:

    - **Feature-incomplete:** not all desired features have been completed

    - Black-box testing of the software's features has started

    - Software is expected to have serious bugs that may cause crashes or data loss

    - A small number of intrepid customers might help with testing

2. Beta software:

    - **Feature-complete:** all desired features have been completed, but may still be buggy
    
    - Can be used for product demos, etc.

3. Release candidate:

    - A beta version that is very stable and reliable

    - **Code-complete:** no entirely new code will be added to the software release

4. Release:

    - Software is made generally available to customers

    - Frequently referred to as a "stable release"

Each phase imposes greater strictness on what changes may be made to the code, who is allowed to make them, the review process, etc.

## Release Version Numbers

Software releases are usually assigned a series of version numbers. Examples:

- MacOS X version 10.14.6

- Java development kit version: java version "12" 2019-03-19 (build 12+33)

- Python version: 3.7.4

Rule-of-thumb:

- Changes in leftmost number indicate most significant changes (e.g., changing from Python 2 to Python 3 means your program probably won't work)

- Changes in rightmost number indicate least significant changes (e.g., changing from Python 3.7.2 to 3.7.4 is probably fine)

Common approach: [major].[minor].[point]

- Change in [major] means *backward-incompatible* API change

- Change in [minor] means *backward-compatible* API change

    - e.g., new features exposed via existing API, new APIs

- Change in [point] means bugfixes, performance improvements, etc. but no feature changes

Frequently, the release stage is also indicated: [major].[minor].[point]-[stage]

- e.g., 2.1.5-b4 (beta 4 release of version 2.1.5)

- e.g., 2.1.5-rc1 (release candidate 1 for version 2.1.5)

- e.g., 2.1.5-dev5 (developer-build 5 of upcoming version 2.1.5, for internal distribution and testing only)

When the project reaches a stable release, the "-[stage]" part is dropped.

## Release Branches

Frequently, branches are also used to manage software releases.
When a version of the software has sufficient functionality complete, a **release branch** is created.

- New feature development can continue on the `main` branch

- Only bugfixes and critical features may be added to the release branch code (called **release hardening**)

Of course, changes/fixes on the release branch need to be incorporated back into `main` . . .

As a release solidifies, tags can be used to identify version of the code that are release candidates.
When a release is considered "good enough," this can also be indicated by a tag on the branch.

Simple example: Creating a 1.0.1 point-release.

- Recall: A **point release** is a smaller-scope software release focused on fixing bugs, addressing performance issues. Backward-compatibility with the major release is maintained. No new features, no API changes.

- Idea: Can just create a point release on the same release branch!

    - When it's time for release 2.0, a new rel-2.x release branch can be created from `main`

## The Role of the `main` Branch

Three different philosophies:

1. *"The main branch should fully represent the most recent state of the software project"*

    - Google does this (need to have extensive testing suite to make it possible!)

2. *"Every commit on the master branch should be usable as a release-candidate (beta version of software)"*

    - Github does this

3. *"Every commit on master branch must be release-quality software"*

    - This is probably best for people in academia because users won't know how to clone other versions

## Git Flow

**Git flow** is a very popular Git repo management workflow (see [Vincent Driessen's description](https://nvie.com/posts/a-successful-git-branching-model/)).
It falls into category #3 above (i.e., `main` branch only contains commits that are production ready).

### Structure

- `main` is initially populated with the initial version of the software

- A parallel `develop` branch is where completed features are incorporated into the project

- When develop contains all the necessary features, a new `release` branch is created from `develop`

When a `release` branch is finally ready for release, it is merged to `main` and the merge-commit is tagged with a version number. (Note: Git Flow *always* specifies `--no-ff` on merges).

### Hotfixes 

A **hotfix** is a small software change made to fix a severe problem in a production system

In Git Flow, a hotfix is made off of the `main` branch.

- If there is no `release` branch while the hotfix is being made, the fix is also merged back into `develop`

- Otherwise, the hotfix is merged to `release`

### Feature Branches

Git Flow uses feature branches for all feature development.
When a new feature is to be implemented:
    
- A new branch is created off of `develop`
    
- All development for the feature occurs on that feature branch

Feature branches exist until development of the feature is complete.
Then it is merged back to `develop` (again with `--no-ff`).

Git flow *discourages* pushing feature branches upstream, but many people do this anyways (laptops fall into swimming pools!).

### Final Thoughts

Git Flow is very complex, but it is very organized and popular.
Something like it could be nice for academic projects.

## GitHub Flow

GitHub Flow is a variant of Git Flow that eliminates the `develop` branch (which some say is redundant). 
It continues to use the feature-branch pattern.

GitHub Flow follows these six principles:

1. Anything in `main` is deployable

2. To write new features, create descriptively named branches off `main`

3. Push local feature branches to remote repo constantly

4. When a feature is ready to merge to `main`, create a pull request for it

5. Don't merge the feature into master until it has been reviewed

6. After merging to `main`, deploy the new work to production

### Pull Requests

A **pull request** (PR) is a request for a remote repo to pull specific changes from a local repo.
It is named after the `git request-pull` command, which basically just generates an email to send to the developers (!).

Git repo services like GitHub, GitLab, and Bitbucket have built sophistocated tools to support PRs.

- Can review and comment on the code in a PR

- Can accept or reject PRs

- Can receive notifications regarding PRs

- Can impose restrictions on when PRs may be accepted and who may accept or perform them

## References

- https://githubflow.github.io/

- [Linus on branching](https://blog.plasticscm.com/2010/11/linus-on-branching.html)
