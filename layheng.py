directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
directions_guide = ["up", "down", "left", "right"]


def out_of_bound(game_map, i, j):
    return i < 0 or i > len(game_map) - 1 or j < 0 or j > len(game_map[0]) - 1


def get_head(game_map):
    for i, row in enumerate(game_map):
        for j, val in enumerate(row):
            if val == '@':
                return i, j
    return -1, -1


def get_tail(game_map, i, j, searched):
    for direction in directions:
        tail_i, tail_j = i + direction[0], j + direction[1]
        if not out_of_bound(game_map, tail_i, tail_j) and game_map[tail_i][tail_j] == '#' and not searched[tail_i][
            tail_j]:
            return tail_i, tail_j
    return -1, -1


def update_map(game_map, head_i, head_j, move, searched):
    direction = directions[int(move)]

    prev_i, prev_j = head_i, head_j
    head_i, head_j = head_i + direction[0], head_j + direction[1]
    if out_of_bound(game_map, head_i, head_j) or game_map[head_i][head_j] == 'x' or game_map[head_i][head_j] == '#':
        print("move failed")
        quit()
    game_map[head_i][head_j] = '@'

    while True:
        tail_i, tail_j = get_tail(game_map, prev_i, prev_j, searched)
        if tail_i != -1 or tail_j != -1:
            game_map[prev_i][prev_j] = '#'
            game_map[tail_i][tail_j] = '-'
            searched[prev_i][prev_j] = True
            prev_i, prev_j = tail_i, tail_j
        else:
            break


def solve(game_map, moves):
    for idx, move in enumerate(moves):
        print(f"move {idx + 1}: {directions_guide[int(move)]}")

        searched = [[False for _ in range(len(game_map[0]))] for _ in range(len(game_map))]
        head_i, head_j = get_head(game_map)
        update_map(game_map, head_i, head_j, move, searched)

        for row in game_map:
            print(*row)
        print("move completed", "\n")

    head_i, head_j = get_head(game_map)
    print(f'final coordinate: ({head_i}, {head_j})')


def main():
    game_map = []
    for _ in range(9):
        line = input()
        game_map.append(list(line))

    moves = list(input().split())

    print("map:")
    for row in game_map:
        print(*row)
    print()

    solve(game_map, moves)


if __name__ == "__main__":
    main()
