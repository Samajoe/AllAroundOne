# AllAroundOne

This repository contains a small command-line program to keep track of tasks and notes.

## Usage

```bash
python tasks.py add "Buy milk" --note "Remember lactose-free"
python tasks.py list
python tasks.py note 1 "Bought at corner store"
python tasks.py done 1
python tasks.py remove 1
```

Tasks are stored in `tasks.json` in the repository root.

