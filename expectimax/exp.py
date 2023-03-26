import math

GRAPH = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I", "J"],
}

TERMINALS = {
    "E": [0.5, 3],
    "F": [0.5, 12],
    "G": [0.5, 8],
    "H": [0.5, 2],
    "I": [0.5, 4],
    "J": [0.5, 6],
}

def is_terminal(state):
    return state in TERMINALS

def terminal_value(state):
    return TERMINALS[state][1]

def next_states(state):
    return GRAPH[state]

def avg_value_state(state):
    if (is_terminal(state)):
        return terminal_value(state)
    score = 0
    for move in next_states(state):
        score += max_value_state(move)[1] * TERMINALS[move][0]

    return score

def max_value_state(state):
    if (is_terminal(state)):
        return None, terminal_value(state)
    optimal_value = -math.inf
    best_move = None
    for move in next_states(state):
        value = avg_value_state(move)
        if (value >= optimal_value):
            optimal_value = value
            best_move = move

    return best_move, optimal_value

print(max_value_state("A"))