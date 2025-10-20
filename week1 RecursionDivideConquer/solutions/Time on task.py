"""
Problem: Maximum Tasks Completed Within Time Limit
Approach:
- We use depth-first search (DFS) with backtracking to explore all possible combinations of tasks
- At each step, we have two choices: either take the current task or skip it
- If taking a task would exceed the total available time, we backtrack
- We track the current cumulative time, the current task index, and the count of completed tasks
- The solution explores all possible subsets of tasks to find the maximum number that can be completed
Time Complexity: O(2^n) where n is the number of tasks (exponential)
Space Complexity: O(n) for the recursion stack
"""


def max_tasks_completed(total_time, task_times):
    """
    total_time: Total available time
    task_times: List of time required for each task
    Returns: Maximum number of tasks that can be completed within total_time
    """

    def dfs(current_time, task_index, completed):
        # Base case: if current time exceeds total time, backtrack by reducing count by 1
        if current_time > total_time:
            return completed - 1  # Backtrack one step

        # Base case: if we've considered all tasks, return current count
        if task_index == len(task_times):
            return completed

        # Option 1: Take the current task (if it doesn't exceed time limit)
        # Add current task time and move to next task, increment completed count
        take = dfs(current_time + task_times[task_index], task_index + 1, completed + 1)

        # Option 2: Skip the current task
        # Keep current time unchanged, move to next task, keep completed count same
        skip = dfs(current_time, task_index + 1, completed)

        # Return the maximum of both options
        return max(take, skip)

    # Start DFS with initial time 0, starting from first task, 0 completed tasks
    return dfs(0, 0, 0)


# Read input values
total_time = int(input())  # Total available time
n = int(input())  # Number of tasks
task_times = []  # List to store time required for each task
for i in range(n):
    task_times.append(int(input()))  # Read each task time

# Calculate and print the maximum number of tasks that can be completed
print(max_tasks_completed(total_time, task_times))