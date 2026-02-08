#!/usr/bin/env python3
"""
Task Tracker CLI Application
A simple command-line task management system
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional


class TaskTracker:
    """Main TaskTracker class to manage tasks"""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def _get_next_id(self) -> int:
        """Get the next available task ID"""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def create_task(self, title: str, description: str = "", due_date: str = "") -> Dict:
        """Create a new task"""
        task = {
            'id': self._get_next_id(),
            'title': title,
            'description': description,
            'status': 'pending',
            'due_date': due_date,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        self.tasks.append(task)
        self._save_tasks()
        return task
    
    def view_tasks(self, status_filter: Optional[str] = None, 
                   sort_by_due_date: bool = False) -> List[Dict]:
        """View all tasks with optional filtering and sorting"""
        tasks = self.tasks
        
        # Filter by status if specified
        if status_filter:
            tasks = [t for t in tasks if t['status'] == status_filter]
        
        # Sort by due date if requested
        if sort_by_due_date:
            tasks = sorted(tasks, key=lambda t: t.get('due_date', '9999-12-31'))
        
        return tasks
    
    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as complete"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'complete'
                task['completed_at'] = datetime.now().isoformat()
                self._save_tasks()
                return True
        return False
    
    def edit_task(self, task_id: int, title: Optional[str] = None, 
                  description: Optional[str] = None, 
                  due_date: Optional[str] = None) -> bool:
        """Edit task details"""
        for task in self.tasks:
            if task['id'] == task_id:
                if title is not None:
                    task['title'] = title
                if description is not None:
                    task['description'] = description
                if due_date is not None:
                    task['due_date'] = due_date
                self._save_tasks()
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                self._save_tasks()
                return True
        return False
    
    def search_tasks(self, keyword: str) -> List[Dict]:
        """Search tasks by keyword in title or description"""
        keyword = keyword.lower()
        return [
            task for task in self.tasks
            if keyword in task['title'].lower() or 
               keyword in task.get('description', '').lower()
        ]


def print_tasks(tasks: List[Dict]) -> None:
    """Pretty print tasks"""
    if not tasks:
        print("No tasks found.")
        return
    
    print(f"\n{'ID':<5} {'Status':<12} {'Due Date':<12} {'Title':<30} {'Description':<40}")
    print("-" * 100)
    
    for task in tasks:
        status = task['status'].upper()
        due_date = task.get('due_date', 'N/A')[:10] if task.get('due_date') else 'N/A'
        title = task['title'][:28] + '..' if len(task['title']) > 30 else task['title']
        description = task.get('description', '')[:38] + '..' if len(task.get('description', '')) > 40 else task.get('description', '')
        
        print(f"{task['id']:<5} {status:<12} {due_date:<12} {title:<30} {description:<40}")


def print_help() -> None:
    """Print usage help"""
    help_text = """
Task Tracker - CLI Task Management System

Usage:
    task_tracker.py <command> [arguments]

Commands:
    create <title> [description] [due_date]
        Create a new task
        Example: task_tracker.py create "Buy groceries" "Milk, eggs, bread" "2026-02-15"
    
    list [--status STATUS] [--sort-by-date]
        List all tasks or filter by status (pending/complete)
        Example: task_tracker.py list
        Example: task_tracker.py list --status pending
        Example: task_tracker.py list --sort-by-date
    
    complete <task_id>
        Mark a task as complete
        Example: task_tracker.py complete 1
    
    edit <task_id> [--title TITLE] [--description DESC] [--due-date DATE]
        Edit task details
        Example: task_tracker.py edit 1 --title "Buy groceries and supplies"
    
    delete <task_id>
        Delete a task
        Example: task_tracker.py delete 1
    
    search <keyword>
        Search tasks by keyword
        Example: task_tracker.py search "groceries"
    
    help
        Show this help message
"""
    print(help_text)


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    
    tracker = TaskTracker()
    command = sys.argv[1].lower()
    
    try:
        if command == 'create':
            if len(sys.argv) < 3:
                print("Error: Title is required")
                sys.exit(1)
            
            title = sys.argv[2]
            description = sys.argv[3] if len(sys.argv) > 3 else ""
            due_date = sys.argv[4] if len(sys.argv) > 4 else ""
            
            task = tracker.create_task(title, description, due_date)
            print(f"✓ Task created successfully (ID: {task['id']})")
            print(f"  Title: {task['title']}")
            if description:
                print(f"  Description: {description}")
            if due_date:
                print(f"  Due Date: {due_date}")
        
        elif command == 'list':
            status_filter = None
            sort_by_date = False
            
            i = 2
            while i < len(sys.argv):
                if sys.argv[i] == '--status' and i + 1 < len(sys.argv):
                    status_filter = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] == '--sort-by-date':
                    sort_by_date = True
                    i += 1
                else:
                    i += 1
            
            tasks = tracker.view_tasks(status_filter, sort_by_date)
            print_tasks(tasks)
        
        elif command == 'complete':
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            
            task_id = int(sys.argv[2])
            if tracker.mark_complete(task_id):
                print(f"✓ Task {task_id} marked as complete")
            else:
                print(f"✗ Task {task_id} not found")
        
        elif command == 'edit':
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            
            task_id = int(sys.argv[2])
            title = None
            description = None
            due_date = None
            
            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == '--title' and i + 1 < len(sys.argv):
                    title = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] == '--description' and i + 1 < len(sys.argv):
                    description = sys.argv[i + 1]
                    i += 2
                elif sys.argv[i] == '--due-date' and i + 1 < len(sys.argv):
                    due_date = sys.argv[i + 1]
                    i += 2
                else:
                    i += 1
            
            if tracker.edit_task(task_id, title, description, due_date):
                print(f"✓ Task {task_id} updated successfully")
            else:
                print(f"✗ Task {task_id} not found")
        
        elif command == 'delete':
            if len(sys.argv) < 3:
                print("Error: Task ID is required")
                sys.exit(1)
            
            task_id = int(sys.argv[2])
            if tracker.delete_task(task_id):
                print(f"✓ Task {task_id} deleted successfully")
            else:
                print(f"✗ Task {task_id} not found")
        
        elif command == 'search':
            if len(sys.argv) < 3:
                print("Error: Search keyword is required")
                sys.exit(1)
            
            keyword = sys.argv[2]
            tasks = tracker.search_tasks(keyword)
            print(f"Search results for '{keyword}':")
            print_tasks(tasks)
        
        elif command == 'help':
            print_help()
        
        else:
            print(f"Unknown command: {command}")
            print_help()
            sys.exit(1)
    
    except ValueError as e:
        print(f"Error: Invalid argument - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
