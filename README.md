
# UGM_Calculator

## About the Project
UGM_Calculator is a group project developed by Computing students. Our goal is to build a simple, user-friendly calculator while learning Python, software development and teamwork.


## Project Features

- Addition, subtraction, multiplication and division
- Calculations with decimal and negative numbers
- Parentheses for mathematical expressions
- Result formatting to one decimal place, removing unnecessary trailing zeros
- Clear (C) button to reset the current calculation
- Backspace (⌫) button to remove the last character
- Input validation and error handling, including division by zero
- Calculation history to display previous calculations
- Clear History functionality
- User-friendly desktop graphical interface built with CustomTkinter


## Application Screenshot

The screenshot below shows the completed UGM Calculator desktop application.

![UGM Calculator Desktop Application](docs/screenshots/calculator-screenshot.png)


## Technologies
- **Python** — Main programming language
- **CustomTkinter** — Desktop graphical user interface
- **Git and GitHub** — Version control
- **GitHub Issues** — Task management
- **GitHub Projects** — Progress tracking
- **Pull Requests** — Code review and collaboration


## Project Structure
```text
UGM_calculator/
├── main.py
├── calculator.py
├── gui.py
├── history.py
├── tests/
│   └── test_calculator.py
├── assets/
├── docs/
├── requirements.txt
├── README.md
└── .gitignore
```


### File Responsibilities

- `main.py` — Starts the desktop application.
- `calculator.py` — Contains the calculator's mathematical operations.
- `gui.py` — Contains the graphical user interface.
- `history.py` — Manages calculation history.
- `tests/` — Contains automated tests.
- `assets/` — Stores application images and other visual resources.
- `docs/` — Contains project documentation.
- `requirements.txt` — Lists the required Python packages.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gabrielafranciscato/UGM_Calculator.git
cd UGM_Calculator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```


**Note:** The UGM Calculator is fully functional and can be launched by running `python main.py` after installing the required dependencies.

The application opens a desktop window where users can perform calculations, use parentheses, view calculation history and clear previous entries.

For detailed instructions on using the calculator, refer to the [User Guide](docs/user-guide.md).


## Team Collaboration

Our team uses GitHub to organise tasks, track progress and review code.

Each student should:

1. Work on their assigned task using a separate branch.
2. Follow the project structure and coding conventions.
3. Test their code before submitting changes.
4. Create a Pull Request when their task is ready for review.
5. Wait for approval before merging changes into `main`.

The Team Lead coordinates the project, reviews contributions and supports collaboration between team members.

## Project Status

**Functional Application — Testing and Documentation**

The UGM Calculator has a functional desktop graphical user interface built with Python and CustomTkinter.

The application supports basic arithmetic operations, decimal and negative numbers, parentheses, calculation history, clear and backspace functions, and error handling.

All 10 documented manual test cases have passed successfully.

The project is currently undergoing final documentation review and preparation for the university demonstration.

## Project Purpose

This project is part of our Computing studies and provides practical experience in Python programming, GUI development, version control, testing and collaborative software development.