
# STEP 1. Get input of map and action
# Get input a row at a time

direction = {"up": 0, "down": 1, "left": 2, "right": 3}


def get_input():
    rows = int(input("Enter number of rows: "))

    # Create map list
    game_map = []
    for _ in range(rows):
        row = input()  # Input each row as a line of string
        game_map.append(list(row))  # Append each row as a list of characters

    # get action input
    # split string into list eg. a b c --> ["a", "b", "c"]

    actions = list(map(int, input("Enter Actions: ").split()))

    # Print the game map
    print("Game map:")

    for row in game_map:
        print(*row)
    print("Actions: ", *actions)

    return game_map, actions

# Find name head and body


def find_snake(game_map):

    head_pos = None
    body = []

    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == '@':
                head_pos = (i, j)
            elif game_map[i][j] == '#':
                body.append((i, j))

    if head_pos is None:
        return None, None

    return head_pos, body


def move_snake(game_map, head_pos, body, action):
    x, y = head_pos
    # x,y=rows, cols

    if action == 0:  # move up
        x -= 1
    elif action == 1:  # move down
        x += 1
    elif action == 2:  # turn left
        y -= 1
    elif action == 3:  # turn right
        y += 1

    # check boundaries
    if x < 0 or y < 0 or x >= len(game_map) or y >= len(game_map[0]):
        return None, "Fail"
    # Check for rocks or snake
    if game_map[x][y] == 'x' or (x, y) in body:
        return None, "Fail"

    return (x, y), "Continue"


def game_play(game_map, actions):

    # locate the head
    head_pos, body = find_snake(game_map)
    if not head_pos:
        return "snake head not found!"

    for t, action in enumerate(actions):
        new_head_pos, state = move_snake(game_map, head_pos, body, action)
        if state == "Fail":
            return "Game fail at step {}".format(t+1)

        # move the head
        game_map[head_pos[0]][head_pos[1]] = '#'  # make the old head become body
        game_map[new_head_pos[0]][new_head_pos[1]] = '@'  # Set head to new pos

        # move the body
        if body:
            tail = body.pop()
            game_map[tail[0]][tail[1]] = '-'  # remove one tail
            body.insert(0, head_pos)  # insert old head_pos into body

        # update new head pos of the snake
        head_pos = new_head_pos

        print(f"Step {t+1}: action: {action}")
        for row in game_map:
            print(*row)

    return f"final head position: {head_pos[0]}, {head_pos[1]}"


if __name__ == "__main__":
    game_map, actions = get_input()
    result = game_play(game_map, actions)
    print(result)
