# Task Tracker - GitHub Project Setup Guide

This guide walks you through setting up the complete GitHub Project with Kanban board for the Task Tracker application, following Agile best practices.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [GitHub Project Setup](#github-project-setup)
3. [Kanban Board Configuration](#kanban-board-configuration)
4. [Creating User Stories](#creating-user-stories)
5. [MoSCoW Prioritization](#moscow-prioritization)
6. [Story Points](#story-points)
7. [Iterations (Sprints)](#iterations-sprints)
8. [Milestones](#milestones)
9. [Workflow Management](#workflow-management)
10. [Best Practices](#best-practices)

## Prerequisites

- GitHub account with access to this repository
- Understanding of Agile/Scrum methodology
- Familiarity with Kanban workflow

## GitHub Project Setup

### Step 1: Create a GitHub Project

1. Navigate to GitHub top navigation → Click **Projects**
2. Click **New project**
3. Choose **Board** from the left menu
4. Enter Project name: **Task Tracker - Kanban**
5. Select Visibility: **Public** (for this tutorial)
6. Click **Create**

### Step 2: Link Project to Repository

1. Open your Project
2. Click **⋮** (three dots) → **Settings**
3. Under **Default Repository**, select **task-tracker**
4. Click **Save Changes**

Now issues from this repository can be automatically added to the project.

## Kanban Board Configuration

### Configure Columns

Rename the default columns to match a standard Kanban workflow:

1. **Backlog** - Prioritized ideas and future work
2. **To Do** - Selected for current iteration
3. **In Progress** - Actively being worked on
4. **Done** - Completed and merged

### How to Rename Columns

1. Click on the column name
2. Edit the name
3. Press Enter to save

## Creating User Stories

### Using the Template

This repository includes a User Story template at `.github/ISSUE_TEMPLATE/user-story---title-.md`.

### Create a New User Story

1. Go to repository → **Issues** → **New issue**
2. Select **User Story: <Title>** template
3. Fill in the template:
   ```
   As a <type of user>
   I want <some goal>
   So that <some benefit>
   ```
4. Add acceptance criteria
5. Click **Create**

### Example User Stories

#### User Story #1: Create a Task
```
As a user
I want to create a new task
So that I can track what I need to do

Acceptance Criteria:
- User can access a "Create Task" form
- User can enter task title and description
- User can save the task
- Task appears in the task list after creation
```

#### User Story #2: View Task List
```
As a user
I want to see a list of all my tasks
So that I know what needs to be done

Acceptance Criteria:
- User can view all created tasks
- Tasks display title and status
- List updates when tasks are added or removed
```

#### User Story #3: Mark Task as Complete
```
As a user
I want to mark a task as complete
So that I can track my progress

Acceptance Criteria:
- User can click a checkbox or button to mark task complete
- Completed tasks are visually distinguished
- Task status persists after page refresh
```

#### User Story #4: Delete a Task
```
As a user
I want to delete a task
So that I can remove tasks I no longer need

Acceptance Criteria:
- User can click a delete button on each task
- System prompts for confirmation
- Task is removed from the list after deletion
```

## MoSCoW Prioritization

MoSCoW is a prioritization technique that categorizes requirements into four groups:

### Creating Labels

1. Go to Repository → **Issues** → **Labels**
2. Click **New label** for each priority level

### Label Definitions

| Label Name | Description | Color | Hex Code |
|------------|-------------|-------|----------|
| **Must Have** | Critical for MVP | Red | #FF0000 |
| **Should Have** | Important but not critical | Orange | #FFA500 |
| **Could Have** | Nice to have | Yellow | #FFFF00 |
| **Won't Have** | Out of scope for now | Grey | #808080 |

### Assigning Labels

1. Open a user story (issue)
2. Click **Labels** in the right sidebar
3. Select the appropriate MoSCoW label

### Example Assignments

| User Story | Priority |
|------------|----------|
| Create a new task | Must Have |
| View Task List | Must Have |
| Mark Task as Complete | Should Have |
| Delete a task | Could Have |

## Story Points

Story points represent the relative effort required to complete a user story.

### Creating Story Points Field

1. Open the Project → **⋮** (three dots) → **Settings**
2. Click **New field** (+)
3. Configure:
   - **Name**: Story Points
   - **Type**: Number
4. Click **Save**

### Fibonacci Scale

Use the Fibonacci sequence for estimation:

| Points | Effort Level | Time Estimate |
|--------|--------------|---------------|
| 1 | Very small | < 1 hour |
| 2 | Small | 1-2 hours |
| 3 | Medium | Half day |
| 5 | Large | 1 day |
| 8 | Very large | 2-3 days |
| 13 | Too big | Should be split |

### Assigning Story Points

1. Open the user story in the project board
2. Find the **Story Points** field
3. Enter the estimated points

### Example Assignments

| User Story | Story Points | Rationale |
|------------|--------------|-----------|
| Create a new task | 5 | Includes form, validation, and backend integration |
| View Task List | 3 | Display logic and UI components |
| Mark Task as Complete | 3 | State management and UI updates |
| Delete a task | 2 | Simple CRUD operation with confirmation |

## Iterations (Sprints)

Iterations (sprints) are time-boxed periods for completing work.

### Creating Iteration Field

1. Open the Project → **⋮** (three dots) → **Settings**
2. Click **New field** (+)
3. Configure:
   - **Field Type**: Iteration
   - **Name**: Sprint
   - **Duration**: 2 weeks (recommended)
   - **Start date**: Choose a Monday
4. Click **Save and Create**

### Example Sprint Setup

| Sprint | Date Range | Story Points |
|--------|------------|--------------|
| Sprint 1 | Feb 9 - Feb 22 | 8 points |
| Sprint 2 | Feb 23 - Mar 8 | 5 points |

### Sprint 1 Planning

**Goal**: Implement core task creation and viewing functionality

- Create a new task (5 points)
- View Task List (3 points)
- **Total**: 8 story points

### Sprint 2 Planning

**Goal**: Add task management features

- Mark Task as Complete (3 points)
- Delete a task (2 points)
- **Total**: 5 story points

### Assigning Issues to Sprints

1. Open the user story in the project board
2. Find the **Sprint** field
3. Select the appropriate sprint

### Viewing by Sprint

1. Go to Project → **View**
2. Click **Column by** → **Sprint**

This groups issues by sprint for easier sprint planning.

## Milestones

Milestones represent significant goals or releases in your project.

### Creating a Milestone

1. Go to repository → **Issues** → **Milestones**
2. Click **New milestone**
3. Configure:
   - **Title**: MVP v1.0
   - **Description**: Minimum viable product for Task Tracker
   - **Due date**: March 6, 2026
4. Click **Create milestone**

### Assigning Issues to Milestones

1. Open a user story (issue)
2. In the right sidebar, find **Milestone**
3. Select **MVP v1.0**

### Example Milestone Assignment

All four user stories should be assigned to the **MVP v1.0** milestone:
- Create a new task
- View Task List
- Mark Task as Complete
- Delete a task

### Milestone Tracking

GitHub automatically tracks:
- Percentage completed
- Open vs closed issues
- Due date status

### Viewing Milestones in Project

1. Open Project → **View settings**
2. Click **Fields**
3. Select **Milestone** field
4. Save view

Now you can filter and group by milestone in your project board.

## Workflow Management

### Issue Lifecycle

```
Create Issue → Backlog → To Do → In Progress → Done
```

### Moving Issues Through the Board

#### Method 1: From Issue Page

1. Open the issue
2. Find **Projects** section (right sidebar)
3. Select the project
4. Change **Status** field to desired column

#### Method 2: Drag and Drop

1. Open the project board
2. Locate the issue card
3. Drag and drop to the desired column

### Automatic Transitions

GitHub automatically moves issues to **Done** when:
- Linked Pull Request is merged
- Issue is manually closed

### Project Automation

Configure automation in Project Settings → **Workflows**:

- **Auto-add new issues**: Automatically add new issues to Backlog
- **Auto-close completed items**: Move to Done when PR is merged
- **Auto-archive closed items**: Archive items after they've been Done for a period

## Best Practices

### Sprint Planning

1. **Review Backlog**: Prioritize and groom backlog items
2. **Select Work**: Choose items that fit sprint capacity
3. **Estimate Points**: Ensure total points are realistic
4. **Set Goals**: Define clear sprint objectives

### During Sprint

1. **Daily Updates**: Move cards through the board daily
2. **Track Progress**: Monitor story point burndown
3. **Communicate Blockers**: Flag issues early
4. **Focus on Completion**: Finish items before starting new ones

### Sprint Review

1. **Demo Work**: Show completed functionality
2. **Gather Feedback**: Collect stakeholder input
3. **Update Documentation**: Keep docs current
4. **Retrospective**: Discuss what went well and what to improve

### Using Filters and Views

Create custom views for different perspectives:

#### View by Sprint
- Click **Column by** → **Sprint**
- See all issues grouped by sprint

#### View by Priority
- Click **Slice by** → **Labels**
- Filter for Must Have items

#### View Completed Work
- Filter: **Status** = Done
- See all completed items

### Combining Tools

Use all tools together for comprehensive project management:

| Tool | Purpose |
|------|---------|
| **Kanban Columns** | Track daily work status |
| **Iterations** | Plan time-boxed work |
| **Story Points** | Estimate effort |
| **MoSCoW Labels** | Prioritize scope |
| **Milestones** | Track release goals |

### Example Combined Usage

For **Sprint 1** of **MVP v1.0**:
- Filter: Milestone = MVP v1.0 AND Sprint = Sprint 1
- View: Must Have and Should Have items
- Track: Story points total (should not exceed team capacity)
- Monitor: Status through Kanban columns

## Troubleshooting

### Issue Not Appearing in Project

**Solution**: Manually add the issue
1. Open the issue
2. Right sidebar → **Projects**
3. Select **Task Tracker - Kanban**
4. Set Status to appropriate column

### Cannot See Custom Fields

**Solution**: Show fields in view
1. Project → **View settings**
2. Click **Fields**
3. Check the fields you want to display

### Automation Not Working

**Solution**: Check automation settings
1. Project → **Settings** → **Workflows**
2. Verify automation rules are enabled
3. Check if conditions match your workflow

## Summary

This comprehensive setup provides:

✅ **Kanban board** for visual workflow management  
✅ **User stories** as structured requirements  
✅ **MoSCoW prioritization** for scope management  
✅ **Story points** for effort estimation  
✅ **Iterations** for time-boxed planning  
✅ **Milestones** for release tracking  

By combining these tools, you have a complete Agile project management system within GitHub.

---

**Tutorial Credit**: Munawar Nadeem© v1.0 - WAES Full Stack Bootcamp
