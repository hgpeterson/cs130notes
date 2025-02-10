# Version Control / Git 101 : Advanced Git Features

## Tagging Versions of the Code

Many VCSs support **tagging** a specific version of the code-base.
*Tags pushed to other repos are generally expected to **never change**.*

Some Git commands:

- `git tag <tagname>` creates the specified tag in the local repo

- `git tag` lists all tags in the local repo

- `git tag -d <tagname>` deletes a tag from the local repo

- `git checkout <tagname>` retrieves a tagged version of the repo (tags just specify a name for a specific commit)

- `git push` *does not* automatically propagate tags to remote repos.

    - `git push --tags` propagates *all* local tags to a remote repo

    - `git push <remote> <tagname>` propagates the specified tag (plus all relevant commits) to a remote repo

- `git pull` will pull *all* tags from the remote repo (`git pull --no-tags` will not pull new tags).

*Note:* While a tag is only on your local system, feel free to manipulate it, move it, delete it. **Once you push** the tag to a remote repo, you should view it as **"set in stone."**

## Branches

Many VCSs support **branching** a code base, allowing devs to work on large (possibly destabilizing) features in parallel without affecting the main version of the code.

Some Git commands:

- `git status` reports the branch you are working on

- `git branch <branchname>` creates a branch

- `git checkout <branchname>` switches to a branch

    - `git checkout -b <branchname>` creates a new branch and switches to it in one step

- `git branch` (or `git branch --list`) lists all branches in local repo

- `git branch -d <branchname>` deletes a branch from your local repo

    - This *does not* delete the commits on the branch. Git "branches" are simply *labels* pointing to the last commit on each branch. "Deleting a branch" just removes the label.

### Use

Common scenario: Adding a new feature to a code-base that requires significant reworking, almost certainly breaking the project on the way. Remember:

> *"Don't break the build!"*

Always keep the code on `main` at a high level of quality!

A common approach: Create a branch to develop the feature on.

- `git checkout -b risky-feature`

This is called **feature branching**.

### Pushing

When you `git push` from a local branch to a remote repo:

- If the remote repo already has a branch of that name, your commits will be propagated to that branch

- Otherwise, a new remote branch must be created

    - Git will prompt you with the arguments to do this, e.g. `--set-upstream`

### Checking out

Can also check out branches from the remote server, e.g., that others created.

- *Note:* `git branch --list` doesn't list remote branches!

- `git branch --list -a` lists all branches, including remote

- `git branch --list -r` lists only remote branches

### Merging

As work on a branch proceeds, an **issue** develops over time: changes in `main` could affect development on the feature and should be incorporated! 
Need to **merge** the changes.

- `git merge main` merges changes from `main` to the feature branch (do this from the feature branch!)

Each merge generate a new **merge-commit**.
As with regular commits, can generate **merge conflicts**.

- `git status` to see which files have merge conflicts to resolve

- `git add` each file after resolving

- `git commit` to complete the merge 

When the new feature is finished and ready to incorporate into `main`, switch back to `main` and merge in feature branch:

- `git checkout main`

- `git merge risky-feature`

If the feature branch is no longer needed, it should be deleted.

If you are the only one working on a project you'll probably only be on the feature branch, not making changes to `main`.
When you merge the changes, Git will perform a **fast-forward merge** and no merge-commit is created. 
(You can force Git to *not* fast-forward with `git merge --no-ff <branchname>`).

### Rebasing

Regular merges generate extra commits in the repo history.
Instead, **rebasing** replays the entire branch's changes against the most recent commit.

This *re-writes history*, so be careful! 

> **Golden Rule of Rebasing:** *Never use rebase on a public branch.*

Otherwise, someone could have pulled the commits that would be rewritten by a rebase.

A scenario in which rebasing is useful:

1. You are working on a feature branch . . .

2. Important, relevant commits have been made to what your branch is based on . . .

    - e.g., you branched off of `main` and important bug-fixes or features were added on `main` to help you complete your work

3. Your branch is still *local only* (SAFE) or you *know* no one has done any work against it (DANGEROUS)

### Git Pull—Merge or Rebase?

`git pull --merge` is the default, but should you `git pull --rebase`?

You should follow the Golden Rule of Rebasing above.
One scenario in which rebasing makes sense:

- You checked out a branch and develop locally

- At the same time, other devs are also pushing changes

- You `git pull`, so now Git has to figure out how to combine the changes

    - By default, it merges to `main`, producing a complicated history

Since no one has seen your local changes yet, rebasing is a good option.
`git pull --rebase` will create a nice linear commit history. 
You can make this the default behavior with
```
git config --global pull.rebase true
```
