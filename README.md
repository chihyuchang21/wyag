# WYAG — Write Your A Git

**WYAG** (short for “Write Your A** Git”) is a minimal reimplementation of Git written in Python.  
In large-scale enterprise environments where thousands of developers frequently contribute to shared codebases, 
following the team’s Git workflows is critical—especially for new engineers. 
For me, understanding the **underlying logic and mechanics behind Git operations** is key to building confidence and contributing effectively.  
That's why I followed the excellent [WYAG tutorial](https://wyag.thb.lt/) to learn how Git works from the inside out, by implementing a simplified version myself.

---

## Features

WYAG supports a subset of Git's core commands, implemented in pure Python:

| Command         | Description                                               |
|-----------------|-----------------------------------------------------------|
| `init`          | Initialize a new Git repository                          |
| `add`           | Add files to the staging area (index)                    |
| `commit`        | Commit staged changes to the repository                  |
| `cat-file`      | Display the raw content of Git objects                   |
| `hash-object`   | Compute SHA-1 hash of a file and optionally store it     |
| `log`           | Show commit history (Graphviz-style)                     |
| `ls-tree`       | List the contents of a tree object                       |
| `checkout`      | Restore files from a commit into a working directory     |
| `status`        | Show working tree status                                 |
| `tag`           | List or create lightweight/annotated tags                |
| `show-ref`      | Display all references (branches, tags, etc.)            |
| `rev-parse`     | Resolve references (HEAD, tags, branches, etc.)          |
| `ls-files`      | Show files currently tracked by the index                |
| `check-ignore`  | Check which files are ignored by Git                     |
| `rm`            | Remove files from the working tree and index             |

---

## Quick Start

```bash
# Initialize a repo
python wyag.py init my-repo
cd my-repo

# Create a file and add it
echo "Hello" > hello.txt
python ../wyag.py add hello.txt

# Commit the change
python ../wyag.py commit -m "First commit"
```


## Reflections & Notes

- **`argparse`**: This project makes extensive use of `argparse` to support subcommands like `init`, `add`, `commit`, etc.—just like Git CLI. I learned how to structure subcommands with `add_subparsers()` and assign arguments per command in a clean, scalable way.
- **Repository structure**: I now understand how Git initializes and organizes its `.git` folder: including how `HEAD`, `config`, `refs/heads`, and `objects` are constructed and connected.
- **Object model**: Through implementing `blob`, `tree`, and `commit` object classes, I got a much clearer picture of how Git stores content as compressed, hashed objects and links them through commits.
- **Serialization**: I implemented Git’s internal data format parsing (like `kvlm` for commit metadata) and gained experience writing custom (de)serialization logic in Python.
- **SHA-1 and zlib**: I learned how Git uses `hashlib` to generate object IDs via SHA-1 and compresses data with `zlib` before storing.
- **Graph traversal**: The `log` command visualizes commit history via Graphviz, helping me understand parent pointers and commit ancestry in Git.
- **Working directory vs. index vs. HEAD**: This was a key insight. The `status` implementation showed how Git tracks what’s changed but not staged, staged but not committed, and already committed.

These insights help demystify Git behavior during real-world development—for example, why certain merge conflicts occur, or why `git status` might show unexpected changes. More importantly, this project deepened my appreciation of the design choices that make Git both powerful and complex.
