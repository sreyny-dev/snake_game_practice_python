import numpy as np


def get_input():
    # Step 1: Get the map input
    rows = int(input("Enter the number of rows in the map: "))
    cols = int(input("Enter the number of columns in the map: "))

    print("Enter the map row by row (x for rock, - for space, # for body, @ for head):")

    map_list = []
    for _ in range(rows):
        row = input()  # Input each row as a string
        map_list.append(list(row))  # Convert the row to a list of characters

    # Convert map_list to a NumPy array
    game_map = np.array(map_list)

    # Step 2: Get the action input
    actions = list(map(int, input(
        "Enter the action sequence (0 for up, 1 for down, 2 for left, 3 for right) separated by spaces: ").split()))

    return game_map, actions


def find_snake_head(game_map):
    # Find the position of the snake's head (marked by '@')
    for i in range(game_map.shape[0]):
        for j in range(game_map.shape[1]):
            if game_map[i, j] == '@':
                return (i, j)
    return None


def move_snake(game_map, head_pos, action):
    """Move snake based on the action. Return new head position and game state."""
    x, y = head_pos
    if action == 0:  # Move up
        x -= 1
    elif action == 1:  # Move down
        x += 1
    elif action == 2:  # Move left
        y -= 1
    elif action == 3:  # Move right
        y += 1

    # Check boundaries
    if x < 0 or x >= game_map.shape[0] or y < 0 or y >= game_map.shape[1]:
        return None, "Fail"

    # Check for rocks or snake's own body
    if game_map[x, y] == 'x' or game_map[x, y] == '#':
        return None, "Fail"

    # Move the snake
    return (x, y), "Continue"


def simulate_game(game_map, actions):
    # Find the snake's starting head position
    head_pos = find_snake_head(game_map)
    if not head_pos:
        print("No snake head found.")
        return

    for t, action in enumerate(actions):
        head_pos, state = move_snake(game_map, head_pos, action)
        if state == "Fail":
            print(f"Game over at time step {t + 1}")
            return

        # Update the map with the new head position
        game_map[game_map == '@'] = '-'  # Clear old head position
        game_map[head_pos] = '@'  # Set new head position

    print(f"Final head position: {head_pos[0]}, {head_pos[1]}")


# Main code to run the game
game_map, actions = get_input()
simulate_game(game_map, actions)
