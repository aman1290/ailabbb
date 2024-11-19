def minimax(tree, index, is_maximizing_player):
    # Check if it's a leaf node: both left and right children do not exist
    if 2 * index + 1 >= len(tree):
        return tree[index]

    if is_maximizing_player:
        # Maximizing player chooses the maximum value from its children
        left = minimax(tree, 2 * index + 1, False)
        right = minimax(tree, 2 * index + 2, False)
        return max(left, right)
    else:
        # Minimizing player chooses the minimum value from its children
        left = minimax(tree, 2 * index + 1, True)
        right = minimax(tree, 2 * index + 2, True)
        return min(left, right)

tree = [1, 3, 2, 5, 6, 9, 8, 7, 4]

# Find the best value for the maximizing player starting from the root (index 0)
best_value = minimax(tree, 0, True)
print(f"Best value from the root is: {best_value}")
