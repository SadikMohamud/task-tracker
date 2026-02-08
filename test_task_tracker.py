#!/usr/bin/env python3
"""
Unit tests for Task Tracker CLI Application
"""

import unittest
import os
import json
import tempfile
from task_tracker import TaskTracker


class TestTaskTracker(unittest.TestCase):
    """Test cases for TaskTracker class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.test_file.close()
        self.tracker = TaskTracker(data_file=self.test_file.name)
    
    def tearDown(self):
        """Clean up test fixtures"""
        # Remove the temporary file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_create_task(self):
        """Test creating a new task"""
        task = self.tracker.create_task("Test Task", "Test Description", "2026-02-15")
        
        self.assertEqual(task['id'], 1)
        self.assertEqual(task['title'], "Test Task")
        self.assertEqual(task['description'], "Test Description")
        self.assertEqual(task['status'], 'pending')
        self.assertEqual(task['due_date'], "2026-02-15")
        self.assertIsNotNone(task['created_at'])
        self.assertIsNone(task['completed_at'])
    
    def test_create_multiple_tasks(self):
        """Test creating multiple tasks with auto-incrementing IDs"""
        task1 = self.tracker.create_task("Task 1")
        task2 = self.tracker.create_task("Task 2")
        task3 = self.tracker.create_task("Task 3")
        
        self.assertEqual(task1['id'], 1)
        self.assertEqual(task2['id'], 2)
        self.assertEqual(task3['id'], 3)
    
    def test_view_tasks(self):
        """Test viewing all tasks"""
        self.tracker.create_task("Task 1")
        self.tracker.create_task("Task 2")
        
        tasks = self.tracker.view_tasks()
        self.assertEqual(len(tasks), 2)
    
    def test_mark_complete(self):
        """Test marking a task as complete"""
        task = self.tracker.create_task("Task to Complete")
        
        result = self.tracker.mark_complete(task['id'])
        self.assertTrue(result)
        
        # Verify the task is marked as complete
        updated_task = next(t for t in self.tracker.tasks if t['id'] == task['id'])
        self.assertEqual(updated_task['status'], 'complete')
        self.assertIsNotNone(updated_task['completed_at'])
    
    def test_mark_complete_nonexistent(self):
        """Test marking a non-existent task as complete"""
        result = self.tracker.mark_complete(999)
        self.assertFalse(result)
    
    def test_edit_task_title(self):
        """Test editing a task's title"""
        task = self.tracker.create_task("Original Title")
        
        result = self.tracker.edit_task(task['id'], title="Updated Title")
        self.assertTrue(result)
        
        updated_task = next(t for t in self.tracker.tasks if t['id'] == task['id'])
        self.assertEqual(updated_task['title'], "Updated Title")
    
    def test_edit_task_description(self):
        """Test editing a task's description"""
        task = self.tracker.create_task("Task", "Original Description")
        
        result = self.tracker.edit_task(task['id'], description="Updated Description")
        self.assertTrue(result)
        
        updated_task = next(t for t in self.tracker.tasks if t['id'] == task['id'])
        self.assertEqual(updated_task['description'], "Updated Description")
    
    def test_edit_task_due_date(self):
        """Test editing a task's due date"""
        task = self.tracker.create_task("Task", "", "2026-02-15")
        
        result = self.tracker.edit_task(task['id'], due_date="2026-03-01")
        self.assertTrue(result)
        
        updated_task = next(t for t in self.tracker.tasks if t['id'] == task['id'])
        self.assertEqual(updated_task['due_date'], "2026-03-01")
    
    def test_edit_nonexistent_task(self):
        """Test editing a non-existent task"""
        result = self.tracker.edit_task(999, title="New Title")
        self.assertFalse(result)
    
    def test_delete_task(self):
        """Test deleting a task"""
        task = self.tracker.create_task("Task to Delete")
        
        result = self.tracker.delete_task(task['id'])
        self.assertTrue(result)
        self.assertEqual(len(self.tracker.tasks), 0)
    
    def test_delete_nonexistent_task(self):
        """Test deleting a non-existent task"""
        result = self.tracker.delete_task(999)
        self.assertFalse(result)
    
    def test_filter_by_status(self):
        """Test filtering tasks by status"""
        task1 = self.tracker.create_task("Task 1")
        task2 = self.tracker.create_task("Task 2")
        self.tracker.mark_complete(task1['id'])
        
        pending_tasks = self.tracker.view_tasks(status_filter='pending')
        complete_tasks = self.tracker.view_tasks(status_filter='complete')
        
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(len(complete_tasks), 1)
        self.assertEqual(pending_tasks[0]['id'], task2['id'])
        self.assertEqual(complete_tasks[0]['id'], task1['id'])
    
    def test_sort_by_due_date(self):
        """Test sorting tasks by due date"""
        self.tracker.create_task("Task 3", "", "2026-03-01")
        self.tracker.create_task("Task 1", "", "2026-01-01")
        self.tracker.create_task("Task 2", "", "2026-02-01")
        
        sorted_tasks = self.tracker.view_tasks(sort_by_due_date=True)
        
        self.assertEqual(sorted_tasks[0]['due_date'], "2026-01-01")
        self.assertEqual(sorted_tasks[1]['due_date'], "2026-02-01")
        self.assertEqual(sorted_tasks[2]['due_date'], "2026-03-01")
    
    def test_search_tasks_by_title(self):
        """Test searching tasks by title"""
        self.tracker.create_task("Buy groceries")
        self.tracker.create_task("Buy milk")
        self.tracker.create_task("Write report")
        
        results = self.tracker.search_tasks("buy")
        self.assertEqual(len(results), 2)
    
    def test_search_tasks_by_description(self):
        """Test searching tasks by description"""
        self.tracker.create_task("Task 1", "Contains keyword")
        self.tracker.create_task("Task 2", "No match here")
        
        results = self.tracker.search_tasks("keyword")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Task 1")
    
    def test_search_case_insensitive(self):
        """Test that search is case insensitive"""
        self.tracker.create_task("UPPERCASE TASK")
        self.tracker.create_task("lowercase task")
        
        results = self.tracker.search_tasks("TASK")
        self.assertEqual(len(results), 2)
    
    def test_persistence(self):
        """Test that tasks are persisted to file"""
        self.tracker.create_task("Persistent Task")
        
        # Create a new tracker instance with the same file
        new_tracker = TaskTracker(data_file=self.test_file.name)
        
        self.assertEqual(len(new_tracker.tasks), 1)
        self.assertEqual(new_tracker.tasks[0]['title'], "Persistent Task")


if __name__ == '__main__':
    unittest.main()
