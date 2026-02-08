# Contributing to Task Tracker

Thank you for your interest in contributing to the Task Tracker project! This document provides guidelines and best practices for contributing.

## 🌟 How to Contribute

### 1. Working on Issues

#### Finding an Issue to Work On

1. Browse the [Project Board](../../projects) to see available work
2. Look for issues in the **To Do** column assigned to the current sprint
3. Check that the issue is not already assigned to someone else
4. Comment on the issue to express interest

#### Starting Work

1. Assign yourself to the issue
2. Move the issue to **In Progress** on the project board
3. Create a new branch from `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/issue-<number>-<short-description>
   ```

Example: `feature/issue-1-create-task`

### 2. Making Changes

#### Code Standards

- Write clean, readable code
- Follow existing code style and conventions
- Add comments for complex logic
- Keep functions small and focused
- Use meaningful variable and function names

#### Commit Messages

Follow the conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(tasks): add create task functionality

Implements the user story for creating new tasks.
Includes form validation and error handling.

Closes #1
```

```
fix(tasks): resolve task deletion bug

Fixed issue where deleted tasks were still visible
in the task list after page refresh.

Fixes #15
```

### 3. Testing Your Changes

Before submitting a pull request:

1. **Test locally**: Ensure your changes work as expected
2. **Check for regressions**: Make sure existing functionality still works
3. **Validate edge cases**: Test with different inputs and scenarios
4. **Review your changes**: Do a self-review of your code

### 4. Creating a Pull Request

#### Pull Request Template

When creating a PR, include:

1. **Title**: Clear, concise description of changes
   - Format: `feat: Add task creation feature` or `fix: Resolve deletion bug`

2. **Description**: Should include:
   - What changes were made
   - Why these changes were made
   - How to test the changes
   - Screenshots (if UI changes)
   - Link to related issue(s)

#### Example PR Description

```markdown
## Changes
Implements the task creation functionality as described in #1.

## Why
This is a Must Have feature for the MVP, allowing users to create new tasks.

## Testing
1. Navigate to the task creation page
2. Fill in the task form
3. Submit the form
4. Verify task appears in the task list

## Screenshots
![Task Creation Form](screenshots/create-task.png)

## Related Issues
Closes #1
```

#### PR Process

1. Create the PR from your feature branch to `main`
2. Link the PR to the related issue(s)
3. Request review from team members
4. The issue will automatically move to **Done** when the PR is merged

### 5. Code Review Process

#### As a Reviewer

- Be constructive and respectful
- Focus on code quality and maintainability
- Check for potential bugs or security issues
- Verify tests are adequate
- Ensure documentation is updated

#### As an Author

- Respond to feedback promptly
- Be open to suggestions
- Make requested changes
- Re-request review after making changes

## 🏷️ Issue Labels

### Priority (MoSCoW)
- **Must Have**: Critical for MVP
- **Should Have**: Important but not critical
- **Could Have**: Nice to have
- **Won't Have**: Out of scope

### Type
- **bug**: Something isn't working
- **enhancement**: New feature or improvement
- **documentation**: Documentation updates
- **question**: Further information is requested

### Status
- **good first issue**: Good for newcomers
- **help wanted**: Extra attention needed
- **in progress**: Currently being worked on
- **blocked**: Waiting on dependencies

## 📊 Story Points

When estimating story points for issues:

- **1 point**: Very simple change, < 1 hour
- **2 points**: Simple change, 1-2 hours
- **3 points**: Moderate complexity, half day
- **5 points**: Complex change, 1 day
- **8 points**: Very complex, 2-3 days
- **13 points**: Too large, should be split

## 🔄 Sprint Workflow

### Sprint Planning

At the start of each sprint:
1. Review backlog items
2. Select items for the sprint
3. Move selected items to **To Do**
4. Ensure story points total is realistic

### During Sprint

- Daily check-ins on progress
- Update issue status regularly
- Move issues through the board columns
- Communicate blockers early

### Sprint Review

At the end of each sprint:
- Demo completed work
- Gather feedback
- Update documentation
- Close completed issues

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Provide constructive feedback
- Focus on what's best for the project
- Be patient with questions

### Communication

- Use GitHub Issues for bug reports and feature requests
- Use Pull Requests for code discussions
- Keep conversations focused and professional
- Tag relevant people with @mentions

## 📚 Resources

- [GitHub Issues Documentation](https://docs.github.com/en/issues)
- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Agile/Scrum Methodology](https://www.scrum.org/resources/what-is-scrum)

## ❓ Questions?

If you have questions about contributing:
1. Check existing issues and documentation
2. Create a new issue with the **question** label
3. Reach out to project maintainers

---

Thank you for contributing to Task Tracker! 🎉
