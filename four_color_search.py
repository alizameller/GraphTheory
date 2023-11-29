from generate_xy import G, points

class Graph:
    def __init__(self, G):
        self.graph = G
        self.available = {}

    def color_vertex(self, v, c, coloring):
        print('color vertex:', v, c)
        coloring[v] = c
        for u in self.graph.neighbors(points[v]):
            vertex_num = points.index(u)
            if coloring[vertex_num] is not None:
                continue
            self.available[vertex_num].discard(c)

        for u in self.graph.neighbors(points[v]):
            vertex_num = points.index(u)
            if coloring[vertex_num] is not None:
                continue
            if not self.available[vertex_num]:
                return False
            elif len(self.available[vertex_num]) == 1:
                print("calling color vertex:", vertex_num)
                if not self.color_vertex(vertex_num, next(iter(self.available[vertex_num])), coloring):
                    return False
        print("returning true from:", v)
        return True

    def save_coloring(self, coloring):
        self.coloring = coloring.copy()

    def dfs(self, v, coloring):
        print('dfs:', v)
        if v >= self.graph.number_of_nodes():
            self.save_coloring(coloring)
            return True
        for c in self.available[v]:
            saved_available_state = {vertex: self.available[vertex].copy() for vertex in self.available}
            saved_coloring_state = coloring.copy()
            if self.color_vertex(v, c, coloring):
                if self.dfs(v + 1, coloring):
                    return True
            self.available = saved_available_state
            coloring = saved_coloring_state
        return False

    def four_color(self):
        self.available = {v: {1, 2, 3, 4} for v in range(self.graph.number_of_nodes())}
        coloring = {v: None for v in range(self.graph.number_of_nodes())}
        
        for v in range(0, 3):
            self.color_vertex(v, 1, coloring)

        if not self.dfs(3, coloring):
            print("No coloring.")
        else:
            # print("Coloring:", self.coloring)
            for vertex, color in self.coloring.items():
                for neighbor in list(self.graph.neighbors(points[vertex])):
                    if color == self.coloring[points.index(neighbor)]:
                        print(vertex, points.index(neighbor))

# Apply Four Coloring algorithm
g = Graph(G)
g.four_color()
