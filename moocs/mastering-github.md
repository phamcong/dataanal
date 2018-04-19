##### (Ref to https://www.dropbox.com/s/v1xu9cot95dgodv/CodeSchool_MasteringGithubCourse.pdf?dl=0) 
### Setting up ``.git-config`` file.
+ ``--local`` to set configuration for a single repo
+ ``--global`` to set configuration for your user
+ ``--system`` to set configuration for all users

#### Setting a configurations
+ Syntax: ``git config --local/--global/--system variable.name(user.name, color.ui, etc.) variable.value(phamcong, true, etc.)``
+ Example: ``git config --global color.ui true``

#### Viewing global configurations
+ Syntax: ``git config --global --list`` or ``cat ~/.gitconfig``
+ Example: ``git config --global --list``

#### Viewing local configurations
This only works within a git repository
+ Syntax: ``git config --local --list`` or ``cat .git/config``
+ Example: ``git config --global --list``

#### Some necessary configurations
+ ``git config --global core.autocrlf input`` (on Linux/Mac); ``git config --global core.autocrlf true`` (on Windows) (Auto carriage return/line feed handling)

+ ``git config --global push.default simple`` (Just pushed current branch to GitHub).

+ ``git config --global push.rebase true`` (Defaults all new branches to fetch then rebase).

+ ``git config --global rerere.enabled true`` (Configuring Reuse Recorded Resolution (ReReRe): Records all fixes to merge conflicts. Reuses them automatically if the same conflict recurs (particulary useful when cherry picking to multiple branches or constantly rebasing).
+ ``git config --global color.ui true``(Configuring output colors).

+ Configuring aliases:
    - ``git config --global alias.s "status -s`` (Configuring alias "git s").
    - ``git config --global alias.lg "log --online --decorate --all --graph`` (Configuring alias "git lg").
