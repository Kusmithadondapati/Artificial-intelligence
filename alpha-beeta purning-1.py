import math

def alpha_beta_pruning(node, alpha, beta, maximizing_player, tree):
    if isinstance(tree[node], int):  
        return tree[node], [node]
    
    best_path = []
    
    if maximizing_player:
        max_value = -math.inf
        for child in tree[node]:
            value, child_path = alpha_beta_pruning(child, alpha, beta, False, tree)
            if value > max_value:
                max_value = value
                best_path = [node] + child_path 
            alpha = max(alpha, value)
            if beta <= alpha:
                break  
        return max_value, best_path
    else:
        min_value = math.inf
        for child in tree[node]:
            value, child_path = alpha_beta_pruning(child, alpha, beta, True, tree)
            if value < min_value:
                min_value = value
                best_path = [node] + child_path  
            beta = min(beta, value)
            if beta <= alpha:
                break  
        return min_value, best_path

game_tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9'],
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}
optimal_value, optimal_path = alpha_beta_pruning('A', -math.inf, math.inf, True, game_tree)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(optimal_path))
