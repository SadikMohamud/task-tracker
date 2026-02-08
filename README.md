# Task Tracker CLI

A simple command-line task management system built with Python. Track your tasks, set due dates, and manage your to-do list efficiently.

## Features

✅ **Must Have**
- **Create a Task**: Add new tasks with title, description, and due date
- **View Task List**: Display all tasks in a formatted table

✅ **Should Have**
- **Mark Task as Complete**: Track task completion status
- **Edit Task Details**: Update task title, description, or due date

✅ **Could Have**
- **Delete a Task**: Remove tasks you no longer need
- **Filter Tasks by Status**: View pending or completed tasks
- **Due Dates for Tasks**: Assign deadlines to your tasks
- **Sort Tasks by Due Date**: See upcoming deadlines first
- **Search Tasks**: Find tasks by keyword in title or description

## Installation

No installation required! Just ensure you have Python 3.6+ installed:

```bash
python3 --version
```

## Usage

### Create a Task

```bash
python3 task_tracker.py create "Task Title" "Optional description" "2026-02-15"
```

Examples:
```bash
# Simple task
python3 task_tracker.py create "Buy groceries"

# Task with description
python3 task_tracker.py create "Buy groceries" "Milk, eggs, bread"

# Task with description and due date
python3 task_tracker.py create "Buy groceries" "Milk, eggs, bread" "2026-02-15"
```

### View All Tasks

```bash
python3 task_tracker.py list
```

### Filter Tasks by Status

```bash
# View only pending tasks
python3 task_tracker.py list --status pending

# View only completed tasks
python3 task_tracker.py list --status complete
```

### Sort Tasks by Due Date

```bash
python3 task_tracker.py list --sort-by-date
```

### Mark Task as Complete

```bash
python3 task_tracker.py complete 1
```

### Edit Task Details

```bash
# Update title
python3 task_tracker.py edit 1 --title "New title"

# Update description
python3 task_tracker.py edit 1 --description "New description"

# Update due date
python3 task_tracker.py edit 1 --due-date "2026-03-01"

# Update multiple fields
python3 task_tracker.py edit 1 --title "Updated title" --description "Updated description"
```

### Delete a Task

```bash
python3 task_tracker.py delete 1
```

### Search Tasks

```bash
python3 task_tracker.py search "keyword"
```

Example:
```bash
python3 task_tracker.py search "groceries"
```

### Help

```bash
python3 task_tracker.py help
```

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically when you add your first task.

## Task Structure

Each task contains:
- **ID**: Unique identifier (auto-generated)
- **Title**: Task title
- **Description**: Optional detailed description
- **Status**: Either "pending" or "complete"
- **Due Date**: Optional deadline (ISO format: YYYY-MM-DD)
- **Created At**: Timestamp when task was created
- **Completed At**: Timestamp when task was marked complete (if applicable)

## Examples

Here's a complete workflow example:

```bash
# Create some tasks
python3 task_tracker.py create "Write report" "Q1 financial report" "2026-02-20"
python3 task_tracker.py create "Team meeting" "Discuss project timeline" "2026-02-10"
python3 task_tracker.py create "Code review" "Review PR #123"

# View all tasks
python3 task_tracker.py list

# View tasks sorted by due date
python3 task_tracker.py list --sort-by-date

# Mark a task as complete
python3 task_tracker.py complete 2

# View only pending tasks
python3 task_tracker.py list --status pending

# Search for tasks
python3 task_tracker.py search "report"

# Edit a task
python3 task_tracker.py edit 1 --due-date "2026-02-25"

# Delete a task
python3 task_tracker.py delete 3
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## License

MIT License - Feel free to use and modify as needed.
