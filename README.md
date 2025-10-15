# Dunders and Decorators Workshop

This repository contains simple, self‑contained Python examples used in a workshop about:
- Dunder methods (aka special methods like `__add__`, `__repr__`, etc.)
- Function decorators and closures

All example code lives in the `src` directory. Use this README to navigate, run, and extend the examples.

## Tech stack
- Language: Python (standard library only)
- Frameworks: none
- Package manager/build system: none (a minimal `requirements.txt` is included)

> TODO: Confirm the exact Python version used during the workshop. The code is plain Python and should run on modern CPython versions.

## Requirements
- Python installed (CPython recommended)
- A terminal (examples below use Windows PowerShell paths/commands)

Optional but recommended:
- Virtual environment (venv)

> No external dependencies are required.

## Package list
- See requirements.txt at the project root. It intentionally has no packages listed because the code and tests only use the Python standard library.

## Getting started
1) Clone or download this repository.
2) (Optional) Create and activate a virtual environment.
   - PowerShell example:
     - python -m venv .venv
     - .\.venv\Scripts\Activate.ps1
3) Run an example script (see options below).

## How to run the examples
You can run any module that has a `if __name__ == "__main__":` block.

From the project root (PowerShell):

- Run the generic sample main:
  - python .\src\main.py

- Dunder examples:
  - python .\src\dunders\dunders_minimal_case.py
  - python .\src\dunders\dunders_basic_example.py

- Decorator/closure examples:
  - python .\src\decorators\inner_outer_func.py
  - python .\src\decorators\decorator_example.py
    - Note: If you encounter a syntax error here, check for any stray characters at the end of the file and remove them. TODO: confirm/fix in source.

You can also run modules using the `-m` flag (module path relative to `src`):
- python -m src.dunders.dunders_minimal_case
- python -m src.dunders.dunders_basic_example
- python -m src.decorators.inner_outer_func
- python -m src.decorators.decorator_example

## Scripts / entry points
There is no package manager configuration or console scripts. The following files can be executed directly:
- src/main.py — simple hello example
- src/dunders/dunders_minimal_case.py — minimal `__add__` implementation demo
- src/dunders/dunders_basic_example.py — broader dunder usage demo
- src/decorators/inner_outer_func.py — closure capturing an outer variable
- src/decorators/decorator_example.py — basic decorator wrapping a function

## Project structure
```
C:\Users\USER\PycharmProjects\DundersAndDecorators
├─ README.md
└─ src
   ├─ main.py
   ├─ dunders
   │  ├─ dunders_basic_example.py
   │  └─ dunders_minimal_case.py
   └─ decorators
      ├─ decorator_example.py
      └─ inner_outer_func.py
```

## Environment variables
- None required.

> TODO: Document any environment variables if future examples are added that need them.

## Tests
- A basic unittest test suite is included under `tests/`.

How to run (from project root):
- Discover and run all tests:
  - python -m unittest discover -s tests -p "test_*.py" -v

Files:
- tests/test_dunders.py — tests minimal dunder example
- tests/test_decorators.py — tests decorators, closures, and Square class

## Keeping the existing example list
The original README listed the examples; that information is preserved and extended here:

- src/dunders
  - dunders_minimal_case.py: Shows a very basic use of `__add__` in a custom class.
  - dunders_basic_example.py: Shows a more comprehensive example with a wider use of dunders.
- src/decorators
  - inner_outer_func.py: Closure example capturing an outer variable.
  - decorator_example.py: Basic decorator with before/after messages.

## License
No license file was found.

> TODO: Add a LICENSE file (e.g., MIT, Apache-2.0) to clarify reuse terms.

## Notes and troubleshooting
- If running a script yields a "module not found" error when using `-m`, ensure you run the command from the project root so that `src` is importable as a top-level package.
- On Windows PowerShell, ensure you use backslashes in paths as shown above.