from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        visited.add(state)
        blank = state.index(0)

        for d in [-3, 3, -1, 1]:  # Moves: up, down, left, right
            new_blank = blank + d
            if 0 <= new_blank < 9 and not (blank % 3 == 0 and d == -1) and not (blank % 3 == 2 and d == 1):
                new_state = list(state)
                new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank]
                new_state = tuple(new_state)
                if new_state not in visited:
                    queue.append((new_state, path + [new_state]))

if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    solution = bfs(start, goal)
    print(f"Solved in {len(solution)} moves!" if solution else "No solution found.")
