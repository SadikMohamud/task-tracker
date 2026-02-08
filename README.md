# Task Tracker Web App

A simple web application for creating, viewing, and managing tasks using GitHub's Kanban project management workflow.

## 📋 Project Overview

This project demonstrates Agile project management using GitHub's built-in features including:
- **GitHub Projects** with Kanban board workflow
- **User Stories** as GitHub Issues
- **MoSCoW Prioritization** via labels
- **Story Points** for effort estimation
- **Iterations (Sprints)** for time-boxed planning
- **Milestones** for release tracking

## 🎯 Project Goal

Build a simple web app where users can:
- ✅ Create new tasks
- 📋 View a list of all tasks
- ✔️ Mark tasks as complete
- 🗑️ Delete tasks they no longer need

## 🗂️ Project Structure

### Kanban Board Columns

Our project board uses a standard Kanban workflow with the following columns:

1. **Backlog** - Prioritized ideas and future work
2. **To Do** - Selected for current iteration/sprint
3. **In Progress** - Actively being worked on
4. **Done** - Completed and merged

### User Stories

User stories are tracked as GitHub Issues using our custom template. Each user story follows the format:

```
As a <type of user>
I want <some goal>
So that <some benefit>
```

Current user stories include:
- **Create a Task** - Allow users to create new tasks
- **View Task List** - Display all tasks to users
- **Mark Task as Complete** - Enable task completion tracking
- **Delete a Task** - Remove unnecessary tasks

## 🏷️ MoSCoW Prioritization

We use MoSCoW labels to prioritize work:

| Label | Description | Priority | Color |
|-------|-------------|----------|-------|
| **Must Have** | Critical for MVP | Highest | 🔴 Red (#FF0000) |
| **Should Have** | Important but not critical | High | 🟠 Orange (#FFA500) |
| **Could Have** | Nice to have | Medium | 🟡 Yellow (#FFFF00) |
| **Won't Have** | Out of scope for now | Low | ⚫ Grey (#808080) |

### Current Prioritization

- **Must Have**: Create a new task, View Task List
- **Should Have**: Mark Task as Complete
- **Could Have**: Delete a task

## 📊 Story Points

We use the Fibonacci sequence for estimating story complexity:

- **1** - Very small
- **2** - Small
- **3** - Medium
- **5** - Large
- **8** - Very large
- **13** - Too big (should be broken down)

### Current Story Points

| User Story | Points | Rationale |
|------------|--------|-----------|
| Create a new task | 5 | Core functionality with form validation |
| View Task List | 3 | Display logic and UI components |
| Mark Task as Complete | 3 | State management and UI update |
| Delete a task | 2 | Simple CRUD operation |

## 🔄 Iterations (Sprints)

We work in 2-week sprints:

### Sprint 1 (Feb 9 - Feb 22)
- Create a new task (5 pts)
- View Task List (3 pts)
- **Total**: 8 story points

### Sprint 2 (Feb 23 - Mar 8)
- Mark Task as Complete (3 pts)
- Delete a task (2 pts)
- **Total**: 5 story points

## 🎯 Milestone: MVP v1.0

**Due Date**: March 6, 2026

**Description**: Minimum viable product for the Task Tracker web app

**Includes**:
- ✅ All Must Have features
- ✅ All Should Have features
- ✅ All Could Have features (if time permits)

## 🚀 Getting Started

### Creating a New User Story

1. Go to the **Issues** tab
2. Click **New Issue**
3. Select the **User Story: <Title>** template
4. Fill in the user story details:
   - Replace `<type of user>` with the user role
   - Replace `<some goal>` with the desired functionality
   - Replace `<some benefit>` with the value it provides
5. Add appropriate labels (MoSCoW priority)
6. Assign to the current sprint/iteration
7. Set story points
8. Link to the milestone (if applicable)

### Workflow

```
Backlog → To Do → In Progress → Done
```

1. **Backlog**: New issues are added here for prioritization
2. **To Do**: Issues selected for the current sprint
3. **In Progress**: Issues actively being worked on
4. **Done**: Issues completed and merged

GitHub automatically moves issues to **Done** when:
- Linked Pull Request is merged
- Issue is manually closed

## 📖 Documentation

- [User Story Template](.github/ISSUE_TEMPLATE/user-story---title-.md)
- [Contributing Guidelines](CONTRIBUTING.md) *(coming soon)*

## 🤝 Contributing

Please refer to our [Contributing Guidelines](CONTRIBUTING.md) for information on how to contribute to this project.

## 📝 License

This is an educational project for the WAES Full Stack Bootcamp.

## 🙏 Acknowledgments

Tutorial created by Munawar Nadeem© for the WAES Full Stack Bootcamp.
