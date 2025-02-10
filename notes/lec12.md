# Version Control / Git 101: Concepts, Basic Git Features

## Version Control Systems

**Version control systems (VCSs)** are the accepted solution to managing files being added/modified/deleted in a coding project, often by multiple people at the same time.
They record every version of every file that is ever part of the project in a single **repository (repo)**.
The latest version of the repo (i.e. the **head**) should always be the most up-to-date, known-good, working version of the software.

*Users don't work on the repository directly!*
Instead they **check out** a local **working copy**.
When the user is satisfied with their changes, they may **commit** (a.k.a. **check in**) them.
Every commit is associated with a **log message**.

### Updating

Developers must periodically **update** their local working copy to incorporate changes made by other developers.

### Merging

If two developers change the same file, then the VCS must **merge** the changes together.
- Usually the VCS can automatically merge multiple changes to the same file (e.g. if two devs edit non-overlapping parts of a file).
- If the VCS cannot automatically merge the edits, it will signal a **merge conflict**.
Then a *human being* must manually merge the changes together and then commit the merged version.

### Other Features

- VCSs can be configured to do things before and/or after committing changes (called **pre-commit / post-commit hooks**).

- Repos can also be locked as read-only or made inaccessible.

### Pitfalls

**When working with multiple devs, it is important to update your local working copy regularly!**
Otherwise:

- Your work will become out of sync

- APIs and functionalities may change

- Merge conflicts will be likely

- It will require increasing effort to incorporate the local work into the repo

In general, try to always work on the most up-to-date version of the code. 
Don't stay on a branch for too long.
*Stay in touch with reality!*

**Keep the repository code high quality (compiling, bug-free, etc.)!**
Otherwise:

- Anyone who fetches your commit will have their local copy broken

- One careless dev can halt an entire team's productivity

> *"Don't break the build!"*

## Distributed VCSs

**Distributed version control systems** = peer-to-peer architecture for version control.

- Devs **clone** a repo from a shared server to their local computer

- When devs want to share their work with others, they can **push** their committed changes to the remote repo

- When devs want to retrieve other committed changes, they can **pull* them from a remote repo

*Donnie tip:* If you ever have to force git, you're doing something wrong!

## Git

**Git** is a *very* widely used distributed VCS developed by Linus Torvalds in 2005.

- It quickly replaced the then-popular Subversion centralized VCS, partly through the creation of sites like GitHub 
    
    - Note: GitHub, GitLab, Bitbucket, etc. are services that provide Git repos along with other tools, e.g., wikis, issue trackers, etc.

- Current estimates: >70% of source code reps use Git

- *Pro Git* book available [online](https://git-scm.com/book/en/v2)

### Command-Line

Virtually all operations are of the form
```
git <command> <options>
```
Git has a very sophistocated command-line help system
```
git help <command> # extensive help docs for each command
git help -a # ALL available commands
```
Example: Cloning a repo
```
git clone git@github.com:pinkston3/stackproc.git
```
- Clones Donnie's stack-processor emulator repo into the local directory `./stackproc`, using SSH key-based authentication

### Staging Area and Commits

The Git repo includes a **staging area** which holds all changes to be included in the next commit operation (commit changes with `git commit`), allowing you to decide what to include in each commit.

*Donnie tip:* Keep your commits small and manageable; don't commits multiple changes at a time!

Add modifies files to staging area with
```
git add file1 file2 ...
```
Add all modified piles in a directory with
```
git add path/to/dir
```
Add and commit in one step
```
git commit -a
```
To see what files are what state
```
git status
```
Will show:
- Untracked files
- Changes not staged for commit
- Changes to be committed

### Pulling Remote Commits

`git pull` retrieves committed work from a remote repo.
Can specify the source repo to pull from, if desired:
```
git pull <remote>
```
By default, changes are pulled from `origin`.
Can use `git remote` to add/remove/list remote repos (e.g. use `git remote -v` to see what repositories can be pulled from).

### Stashing Local Edits

If you have local edits in your working copy but also need to pull, etc., you can **stash** them. 

- `git stash` saves local edits, then restores the working copy to the most recent commit.

- `git stash list` lists all stashes 

- `git stash pop` re-applies the most recent stash

- `git stash drop` discards the most recent stash

### Pushing Local Commits

`git push` pushes committed work from the local repo to a remote repo.

- If there are conflicting commits on the remote repo, a `git pull` may be required first.

As with `git pull`, can specify the remote repo to push to.

## Commit Messages

Every commit is associated with a **log message** describing what changes were made.
This is your opportunity to communicate to your fellow devs/ your future self *why you are making this change.* 
Describe every significant change made and the reasons for them! 

### Git and Commit Messages

Git exposes the commit log via the `git log` command, hence the popular **50/70 format** for commit messages to match logs auto-generated by other Git operations:

- First line of message should be at most 50 characters long

    - This is a *brief summary* of the nature of the change
    - Capitalized
    - Imperative tense 
    - If really necessary, first line can be up to 72 characters, *but no more!*

    Example: "Fix BUG1234: All user data is corrupted"

- If further details are required:

    - Second line should be **blank**
    - Subsequent lines should absolutely respect the 72-character limit
    - Separate paragraphs with blank lines
    - Feel free to use basic markdown, but don't get too involved

## Never Check In. . .

- Passwords, private keys, and other sensitive info

    - If you do this accidentally, it will be available in the revision history for the repo forever (unless you do some very complicated stuff)
    - Safest approach: Assume the information is compromised and go change your passwords, etc.

- Build artifacts such as 

    - Generated source-code documentation
    - Generated binaries
    - Intermediate build artifacts, e.g., `.o` files in C/C++
    - Runtime-generated artifacts, e.g., `.pyc` or `__pycache__` files in Python

- Developer-specific config files

*Remember:* When working with a distributed VCS, if you accidentally commit sensitive data or you completely mangle the local repo, you still have options!
As long as you didn't push the changes to remote, you can always delete the local repo and re-clone.

## `.gitignore`

Many repos provide a mechanism for ignoring files, making it easy to make sure files in your local working copy don't get added to the remote repo.
Git lets you put a `.gitignore` file in any directory of a repo (usually the root) specifying names and file-glob patterns that Git should ignore.
Example:
```
# Don't check in secret info, or local config
secret.py
conf/config-local.json

# Ignore runtime-generated Python bytecode files
# that might appear anywhere in the repository.
**/*.pyc
**/__pycache__

# Ignore macOS Finder droppings
**/.DS_Store
```
Note:

- The `**` wildcard will match zero or more levels of directories
- Relative paths in `.gitignore` are relative to it's location
- Always use forward slashes, even on Windows