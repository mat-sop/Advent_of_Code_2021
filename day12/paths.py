import sys


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_large_cave(self, u):
        return u.isupper()

    def _calculate_all_paths(self, start, dest, visited, path):
        if not self.is_large_cave(start):
            visited[start]= True
        path.append(start)

        if start == dest:
            self._paths.append(path.copy())
        else:
            for i in self.graph[start]:
                if not visited.get(i, False):
                    self._calculate_all_paths(i, dest, visited, path)

        path.pop()
        visited[start]= False


    def get_all_paths(self, start, dest):
        self._paths = []
        self._calculate_all_paths(start, dest, {}, [])
        return self._paths

    def _calculate_all_paths_v2(self, start, dest, visited, path, twice):
        if not self.is_large_cave(start):
            visited[start]= True
        path.append(start)

        if start == dest:
            self._paths.append(path.copy())
        else:
            for i in self.graph[start]:
                if not visited.get(i, False):
                    self._calculate_all_paths_v2(i, dest, visited.copy(), path, twice)
                elif twice and i not in ["start", "end"] and not self.is_large_cave(i):
                    self._calculate_all_paths_v2(i, dest, visited.copy(), path, False)

        path.pop()
        visited[start]= False


    def get_all_paths_v2(self, start, dest):
        self._paths = []
        self._calculate_all_paths_v2(start, dest, {}, [], True)
        return self._paths

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        file_path = "example_input.txt"


    graph = Graph()
    with open(file_path, "r") as f:
        while line := f.readline().strip():
            u, v = line.split("-")
            graph.add_edge(u, v)

    print("### part1")
    paths = graph.get_all_paths("start", "end")
    print(len(paths))


    print("### part2")
    paths_v2 = graph.get_all_paths_v2("start", "end")
    print(len(paths_v2))

