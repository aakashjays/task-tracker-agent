# Task Tracker Agent

A simple yet powerful command-line task management system built in Python. Keep track of your daily tasks, mark them complete, and organize your productivity with ease.

## Features

- ✅ **Add Tasks** - Create new tasks with title, description, and priority
- 🎯 **Mark Complete** - Mark tasks as completed using their unique ID
- 📋 **List Tasks** - View incomplete tasks or all tasks in a clean table format
- 🗑️ **Delete Tasks** - Remove unwanted tasks by their ID
- 💾 **Persistent Storage** - Tasks are automatically saved and persist between sessions
- 🎨 **Beautiful UI** - Clean interface with emojis and color-coded priorities

## Installation

1. Make sure you have Python 3.6+ installed
2. Clone or download the `Task_tracker.py` file
3. Run the application:

```bash
python3 Task_tracker.py
```

## Usage

### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add <title> [description] [priority]` | Add a new task | `add "Buy groceries" "Milk and bread" high` |
| `complete <task_id>` | Mark task as completed | `complete 1753777646963` |
| `list` | Show incomplete tasks | `list` |
| `list all` | Show all tasks | `list all` |
| `delete <task_id>` | Delete a task | `delete 1753777646963` |
| `help` | Show help message | `help` |
| `quit` | Exit application | `quit` |

### Priority Levels

- 🔴 **High** - Important and urgent tasks
- 🟡 **Medium** - Normal priority (default)
- 🟢 **Low** - Less urgent tasks

### Example Session

```
🎯 Welcome to Task Tracker Agent!
==================================================

📋 Available Commands:
1. add <title> [description] [priority] - Add a new task
2. complete <task_id> - Mark task as completed
3. list - Show incomplete tasks
4. list all - Show all tasks
5. delete <task_id> - Delete a task
6. help - Show this help message
7. quit - Exit the application

🤖 Enter command: add "Finish project" "Complete the coding assignment" high
✅ Task added successfully! ID: 1753777646963

🤖 Enter command: list all

All Tasks:
--------------------------------------------------------------------------------
ID           Status     Priority Title                          Description         
--------------------------------------------------------------------------------
1753777646963 ○          🔴        finish_project               complete_the_coding_assignment

🤖 Enter command: complete 1753777646963
✅ Task 1753777646963 marked as completed!

🤖 Enter command: list

Incomplete Tasks:
No tasks found.

🤖 Enter command: quit
👋 Goodbye! Your tasks have been saved.
```

## File Structure

```
Task Tracker/
├── Task_tracker.py    # Main application
├── tasks.json        # Task storage (auto-generated)
└── README.md         # This file
```

## Data Storage

Tasks are automatically saved to `tasks.json` in the same directory as the application. This file is created automatically when you add your first task and persists all your data between sessions.

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This project is open source and available under the MIT License.

---

**Happy Task Tracking! 🎯** 

https://roadmap.sh/projects/task-tracker
