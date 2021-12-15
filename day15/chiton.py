import sys
from dijkstra import Graph, DijkstraSPF
from pprint import pprint


def get_neighbours_coords(x, y, max_x, max_y):
    neighbours = []

    if x == 0:
        neighbours.append((x + 1, y))
    elif x == max_x:
        neighbours.append((x - 1, y))
    else:
        neighbours.append((x - 1, y))
        neighbours.append((x + 1, y))

    if y == 0:
        neighbours.append((x, y + 1))
    elif y == max_y:
        neighbours.append((x, y - 1))
    else:
        neighbours.append((x, y - 1))
        neighbours.append((x, y + 1))
    return neighbours


def build_graph(matrix):
    max_y = len(matrix) - 1
    max_x = len(matrix[0]) - 1
    graph = Graph()
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            for coords in get_neighbours_coords(y, x, max_y, max_x):
                graph.add_edge(str((y, x)), str(coords), matrix[coords[0]][coords[1]])

    return graph

def _add(a, b):
    return a + b if a + b <= 9 else (a+b) % 9

def build_extended_matrix(matrix, times=5):
    extended_matrix = []
    for step in range(times):
        for row in matrix:
            extended_matrix.append([_add(v, step) for v in row])

    for i, row in enumerate(extended_matrix):
        new_row = row.copy()
        for step in range(1, times):
            new_row.extend([_add(v, step) for v in row])
        extended_matrix[i] = new_row

    return extended_matrix

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"

    with open(file_path, "r") as f:
        matrix = [list(map(int, list(line.strip()))) for line in f.readlines()]

    print("### part1")
    start = str((0, 0))
    bottom_right = str((len(matrix) - 1, len(matrix) - 1))
    graph = build_graph(matrix)
    dijkstra = DijkstraSPF(graph, start)
    print(dijkstra.get_distance(bottom_right))

    print("### part2")
    extended_matrix = build_extended_matrix(matrix)
    start = str((0, 0))
    bottom_right = str((len(extended_matrix) - 1, len(extended_matrix) - 1))
    graph = build_graph(extended_matrix)
    dijkstra = DijkstraSPF(graph, start)
    print(dijkstra.get_distance(bottom_right))
