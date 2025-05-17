# Task Tracker

A command-line task tracker that helps you manage your tasks efficiently by allowing you to add, delete, mark as complete or in progress, and persist your task data for continued use.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Command-line Options](#command-line-options)
- [Persistence](#persistence)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Project Link](#project-link)

---

## Features

- **Add Tasks**: Easily add new tasks.
- **Delete Tasks**: Remove tasks you no longer need.
- **Mark Tasks**: Mark tasks as completed, in progress, or to-do.
- **Persistence**: Tasks are saved to a JSON file, ensuring your data is not lost between sessions.
- **View Tasks**: Print a summary of all tasks categorized by status.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/niicommey01/task-tracker.git
   cd task-tracker
   ```

2. **Install using `setup.py`:**
   ```bash
   python3 -m pip install .
   ```

   Or, for development usage:
   ```bash
   python3 setup.py develop
   ```

   > **Requires Python 3.6+**

---

## Usage

After installation, you can use the task tracker from the command line:

```bash
tasktracker [OPTIONS]
```

Or, run directly:
```bash
python tasktracker.py [OPTIONS]
```

---

## Command-line Options

| Option            | Description                                 | Example                          |
|-------------------|---------------------------------------------|-----------------------------------|
| `-a`, `--add_task`        | Add one or more tasks                         | `-a "Buy milk" "Read book"`       |
| `-d`, `--delete_task`     | Delete one or more tasks                      | `-d "Buy milk"`                   |
| `-c`, `--completed`       | Mark tasks as completed                       | `-c "Buy milk"`                   |
| `-p`, `--in_progress`     | Mark tasks as in progress                      | `-p "Read book"`                  |
| `-t`, `--todo`            | Mark tasks as to do                            | `-t "Clean house"`                |

**Examples:**
- Add tasks:  
  `tasktracker -a "Buy groceries" "Call Alice"`
- Mark as completed:  
  `tasktracker -c "Buy groceries"`
- View tasks (shows before and after):  
  `tasktracker`

---

## Persistence

All tasks are stored in `tasktrackerJSON.json` in the project directory. The file is automatically created and updated as you manage your tasks.

---

## Development

- Main module: [`tasktracker.py`](./tasktracker.py)
- Setup file: [`setup.py`](./setup.py)
- Data file: [`tasktrackerJSON.json`](./tasktrackerJSON.json)

**To run locally (for development):**
```bash
python tasktracker.py -a "Sample Task"
```

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For large changes, open an issue to discuss your ideas first.

---

## License

This project is **MIT Licensed**. See `setup.py` for the classifier.

---

## Project Link

- [GitHub Repository](https://github.com/niicommey01/task-tracker)
- [Original Roadmap.sh Project](https://roadmap.sh/projects/task-tracker)

---
