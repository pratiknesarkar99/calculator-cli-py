# Calculator CLI

A command-line calculator built with Python and Click. Supports basic arithmetic
operations, even/odd filtering on addition, and bonus operations like power and
square root.

<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/dc63bc95-6dd0-4410-86af-9f4bed75dd43" />

Built as a portfolio project following the
[App Ideas Collection](https://github.com/florinpop17/app-ideas) Tier 2 spec.

---

## Tech Stack

- **Python 3.11+**
- **Click 8.1+** for CLI parsing
- **pytest** for testing
- **pyproject.toml** for modern Python packaging

---

## Project Structure

```
calculator-cli/
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── cli.py          # Click commands and flags
│       └── operations.py   # Pure math logic, no CLI dependency
├── tests/
│   ├── test_operations.py  # Unit tests for math functions
│   └── test_cli.py         # Integration tests via CliRunner
├── pyproject.toml
└── README.md
```

The core design decision is keeping `operations.py` completely free of Click.
Pure functions only. The CLI layer in `cli.py` handles parsing and delegates
to operations for all computation. This makes the math independently testable
without invoking the CLI at all.

---

## Setup

```bash
git clone <your-repo-url>
cd calculator-cli

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -e ".[dev]"
```

---

## Usage

### Addition

```bash
# Add integers
calc add all 1 2 3
# Result: 6

# Add floats
calc add all 1.5 2.5 -f
# Result: 4.0

# Add only even numbers
calc add even 1 2 3 4 5
# Even numbers: [2, 4]
# Result: 6

# Add only odd numbers
calc add odd 1 2 3 4 5
# Odd numbers: [1, 3, 5]
# Result: 9
```

### Subtraction

```bash
calc sub 10 3 2
# Result: 5

calc sub 10.5 0.5 -f
# Result: 10.0
```

### Multiplication

```bash
calc mul 2 3 4
# Result: 24
```

### Division

```bash
calc div 20 4
# Result: 5.0

calc div 10 0
# Error: Division by zero is not allowed.
```

### Power

```bash
calc pow 2 10
# Result: 1024.0
```

### Square Root

```bash
calc sqrt 9
# Result: 3.0

# Use -- to pass negative numbers (prevents flag parsing)
calc sqrt -- -1
# Error: Cannot take square root of a negative number.
```

---

## Help

Every command and subcommand supports `--help`:

```bash
calc --help
calc add --help
calc add even --help
```

---

## Running Tests

```bash
pytest tests/ -v
```

35 tests covering both the pure math layer and the CLI integration layer.

---

## What This Demonstrates

- **Separation of concerns**: math logic and CLI parsing are fully decoupled
- **Click subcommand groups**: `add` is a group with `all`, `even`, `odd` subcommands
- **Editable installs**: `pip install -e` makes the `calc` binary available globally in the venv
- **CliRunner testing**: click's built-in test utility for integration tests without spawning subprocesses
- **Unix conventions**: errors go to stderr, `--` separates flags from negative number arguments
