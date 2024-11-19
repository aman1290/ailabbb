def alpha_beta_pruning(tree, index, alpha, beta, is_maximizing_player):
    # If it's a leaf node, return its value
    if 2 * index + 1 >= len(tree):  # No children (leaf node)
        return tree[index]

    if is_maximizing_player:
        best = -float('inf')
        # Recur for left and right children
        left = alpha_beta_pruning(tree, 2 * index + 1, alpha, beta, False)
        right = alpha_beta_pruning(tree, 2 * index + 2, alpha, beta, False)
        best = max(left, right)
        alpha = max(alpha, best)
        if beta <= alpha:  # Beta cut-off
            return best
        return best
    else:
        best = float('inf')
        # Recur for left and right children
        left = alpha_beta_pruning(tree, 2 * index + 1, alpha, beta, True)
        right = alpha_beta_pruning(tree, 2 * index + 2, alpha, beta, True)
        best = min(left, right)
        beta = min(beta, best)
        if beta <= alpha:  # Alpha cut-off
            return best
        return best

tree = [1, 3, 2, 5, 6, 9, 8, 7, 4]

# Find the best value for the maximizing player starting from the root (index 0)
best_value = alpha_beta_pruning(tree, 0, -float('inf'), float('inf'), True)
print(f"Best value from the root is: {best_value}")
