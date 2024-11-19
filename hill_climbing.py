def climb(start, func, step=1, max_steps=100):
    current = start
    print(f"Starting point: {current} with value: {func(current)}")
    
    for _ in range(max_steps):
        next_pos = current + step
        print(f"Checking next position: {next_pos} with value: {func(next_pos)}")
        
        if func(next_pos) > func(current):
            current = next_pos
            print(f"Moved to: {current} with value: {func(current)}")
        else:
            print(f"Stopping at: {current} with value: {func(current)}")
            break
    return current

# Example: Maximizing f(x) = -0.1 * (x - 50)^2 + 100
def func(x):
    return -0.1 * (x - 50)**2 + 100

# Start at 0
result = climb(0, func)
print("Best result:", result)
print("Best value:", func(result))
