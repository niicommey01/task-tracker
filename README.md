# 🎉 Task Tracker 🚀

Welcome to **Task Tracker** – your fun, friendly command-line sidekick for conquering your to-do list!  
Add, delete, and organise tasks like a productivity wizard 🧙‍♂️, all while your progress is magically saved for next time.

---

## 🌟 Features

- ➕ **Add tasks** – Because you’re always dreaming up awesome things to do!
- ❌ **Delete tasks** – Out with the old, in with the new.
- ✅ **Mark as complete** – Satisfying, right?
- 🔄 **In progress & To-do** – Organize your journey to greatness.
- 💾 **Persistence** – Your tasks are saved in a handy JSON file. No memory required (for you, at least)!
- 👀 **See your tasks** – Get a colorful summary, anytime.

---

## 🛠️ Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/niicommey01/task-tracker.git
   cd task-tracker
   ```

2. **Install the tracker:**
   ```bash
   python3 -m pip install .
   ```
   _or for development:_
   ```bash
   python3 setup.py develop
   ```

> ⚡ **Requires Python 3.6+**  
> Super easy – get started in under a minute!

---

## 🎲 How to Use

Unleash the power of your terminal:

```bash
tasktracker [OPTIONS]
```

_or run directly:_
```bash
python tasktracker.py [OPTIONS]
```

---

## 📢 Command-line Magic

| Option            | What it does               | Example                              |
|-------------------|---------------------------|--------------------------------------|
| `-a`, `--add_task`      | Add one or more tasks         | `-a "Feed the cat"`                  |
| `-d`, `--delete_task`   | Delete task(s)                | `-d "Feed the cat"`                  |
| `-c`, `--completed`     | Mark as completed             | `-c "Feed the cat"`                  |
| `-p`, `--in_progress`   | Mark as in progress           | `-p "Write README"`                  |
| `-t`, `--todo`          | Mark as to do                 | `-t "Start project"`                 |

**Examples:**
- Add tasks:  
  `tasktracker -a "Learn Python" "Rule the world"`
- Complete a task:  
  `tasktracker -c "Learn Python"`
- See your task list before and after:  
  `tasktracker`

---

## 💾 Where Are My Tasks?

All your tasks (and their glorious states) are saved in `tasktrackerJSON.json` in your project folder.  
No extra setup. No worries.

---

## 👩‍💻 For Developers

- Main script: [`tasktracker.py`](./tasktracker.py)
- Setup file: [`setup.py`](./setup.py)
- Data lives in: [`tasktrackerJSON.json`](./tasktrackerJSON.json)

**Quick run:**
```bash
python tasktracker.py -a "Code like there's no tomorrow."
```

---

## 📝 License

MIT License – free as in fun.

---

## 🌐 Find Us Online

- [GitHub Repo](https://github.com/niicommey01/task-tracker)
- [Original Roadmap.sh Project](https://roadmap.sh/projects/task-tracker)

---

> _Go forth and conquer your tasks – one command at a time! 💪_
