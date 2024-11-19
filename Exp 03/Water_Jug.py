def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    # Stack to store states for DFS (each state is (amount_in_jug1, amount_in_jug2))
    stack = [(0, 0)]
    # Visited set to avoid revisiting states
    visited = set()

    while stack:
        jug1, jug2 = stack.pop()

        # If this state has been visited, skip it
        if (jug1, jug2) in visited:
            continue

        # Mark this state as visited
        visited.add((jug1, jug2))

        # Print the current state
        print(f"Jug1: {jug1}L, Jug2: {jug2}L")

        # Check if we have reached the target amount
        if jug1 == target or jug2 == target or jug1 + jug2 == target:
            print(f"Solution found: Jug1 = {jug1}, Jug2 = {jug2}")
            return True

        # Generate all possible next states and push them onto the stack
        # Fill Jug1
        stack.append((jug1_capacity, jug2))
        # Fill Jug2
        stack.append((jug1, jug2_capacity))
        # Empty Jug1
        stack.append((0, jug2))
        # Empty Jug2
        stack.append((jug1, 0))
        # Pour Jug1 into Jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        stack.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour Jug2 into Jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        stack.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))

    # If we exhaust the stack without finding a solution
    print("No solution exists.")
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_dfs(jug1_capacity, jug2_capacity, target)
'''
Jug1: 0L, Jug2: 0L
Jug1: 0L, Jug2: 3L
Jug1: 3L, Jug2: 0L
Jug1: 3L, Jug2: 3L
Jug1: 4L, Jug2: 2L
Solution found: Jug1 = 4, Jug2 = 2
'''
