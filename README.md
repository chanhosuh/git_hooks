The git hooks will run every time you `git commit` to your local repository.

**Note:** while the sub-hooks for `pre-commit` are for Python, you can replace them with anything you wish.  The sub-hooks are listed in the `pre-commit` file and can easily be edited or removed.  The `commit-msg` hook is not Python-specific amd affects only your commit message.

Installing the hooks:
- copy the hooks to your repo's git hooks directory (`.git/hooks/`)
- make hooks executable (`chmod +x .git/hooks/*`)

Two types of hooks will be installed:

- `commit-msg`:  
  This hook ensures we follow Tim Pope's [guidelines](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) for commit messages:
  - first sentence of the message, the subject, should be at most 50 characters
  - if the message has more than one line, the second line should be blank, to separate the subject from the body of the message
  - the body of the message should be at most 72 characters wide
  
- `pre-commit`:
  There are three Python-specific sub-hooks which will run in the pre-commit stage and must pass before the commit succeeds.
  - isort: sorts your import statements (will reformat and restage your files)
  - black: enforces a strict interpretation of PEP8 (will reformat and restage your files)
  - flake8: fast linting of your code

The `commit-msg` hook will block your commit and you will need to re-edit your message.  It doesn't automatically reformat your message as that would defeat the spirit of the guidelines.

The ideal commit message explains the context of a commit.  The details should be clear from the code change itself.  Remember that commit messages are to help people in the future, including your future self, understand *why* you made the changes you did.

A short subject line is useful when scanning a lot of changes; git itself recommends a short subject line of less than 50 characters (see `git help commit`).  For some simple changes, a short subject alone may be sufficient.

Separating the body of the message from the subject by a blank enables the optimal use of git log utilities.

If these ideas sound unfamiliar, [this article](https://chris.beams.io/posts/git-commit/) is highly recommended.

The `pre-commit` sub-hooks like `isort` and `black` will reformat and restage your files for you, so you never have to worry about formatting your imports or whether you have extra whitespace etc.

`flake8` doesn't reformat your code, so it may fail and reject your commit.  In this case, you should go back and run `flake8` to see what the exact violations are and fix them.
