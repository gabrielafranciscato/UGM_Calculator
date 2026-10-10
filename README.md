
# UGM_Calculator

## About the Project
UGM_Calculator is a group project developed by Computing students. Our goal is to build a simple, user-friendly calculator while learning Python, software development and teamwork.

## Project Features
- Addition, subtraction, multiplication and division
- Clear and backspace buttons
- Error handling, including division by zero
- Simple graphical user interface (GUI)
- Calculation history 

## Technologies
- **Python** — Main programming language
- **CustomTkinter** — Desktop graphical user interface
- **Git and GitHub** — Version control
- **GitHub Issues** — Task management
- **GitHub Projects** — Progress tracking
- **Pull Requests** — Code review and collaboration


## Project Structure
```text
class-python-calculator/
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
git clone https://github.com/gabrielafranciscato/class-python-calculator.git
cd class-python-calculator
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

**Note:** The application is currently in its initial development stage. The main window is available, but the calculator features are still being developed.

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

**In Development — Initial Desktop Application Setup**

The initial Python and CustomTkinter environment has been configured. The next stage is to develop the calculator logic, graphical interface and automated tests.

## Project Purpose

This project is part of our Computing studies and provides practical experience in Python programming, GUI development, version control, testing and collaborative software development.