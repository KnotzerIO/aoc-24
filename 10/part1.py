from heapq import heapify, heappop, heappush
#copied from https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph  # A dictionary for the adjacency list

   def add_edge(self, node1, node2, weight):
       if node1 not in self.graph:  # Check if the node is already added
           self.graph[node1] = {}  # If not, create the node
       self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

   def shortest_distances(self, source: str):
       # Initialize the values of all nodes with infinity
       distances = {node: float("inf") for node in self.graph}
       distances[source] = 0  # Set the source value to 0

       # Initialize a priority queue
       pq = [(0, source)]
       heapify(pq)

       # Create a set to hold visited nodes
       visited = set()

       while pq:  # While the priority queue isn't empty
           current_distance, current_node = heappop(pq)

           if current_node in visited:
               continue
           visited.add(current_node)

           for neighbor, weight in self.graph[current_node].items():
               # Calculate the distance from current_node to the neighbor
               tentative_distance = current_distance + weight
               if tentative_distance < distances[neighbor]:
                   distances[neighbor] = tentative_distance
                   heappush(pq, (tentative_distance, neighbor))

       return distances


def build_graph(graph, matrix, i, j):
    neighbours = {
    }
    def is_valid(pos, neighbour_pos):
        pos = (int(pos[0]), int(pos[1]))
        neighbour_pos = (int(neighbour_pos[0]), int(neighbour_pos[1]))
        if abs(int(matrix[pos[0]][pos[1]]) - int(matrix[neighbour_pos[0]][neighbour_pos[1]])) == 1:
            return True
        return False

    if i > 0 and is_valid((i,j), (i-1,j)):
        neighbour_pos = str(i-1) + "," + str(j)
        neighbours[neighbour_pos] = 1
    if i < len(matrix) - 1 and is_valid((i,j), (i+1,j)):
        neighbour_pos = str(i+1) + "," + str(j)
        neighbours[neighbour_pos] = 1
    if j > 0 and is_valid((i,j), (i,j-1)):
        neighbour_pos = str(i) + "," + str(j-1)
        neighbours[neighbour_pos] = 1
    if j < len(matrix[i]) - 1 and is_valid((i,j), (i,j+1)):
        neighbour_pos = str(i) + "," + str(j+1)
        neighbours[neighbour_pos] = 1

    graph[str(i) + "," + str(j)] = neighbours

file_path = 'input'
with open(file_path, 'r') as file:
    file_content = file.read().split('\n')


matrix = []
for line in file_content:
    matrix.append(list(line))

graph = {}
all_starting_points = []
all_finish_points = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "0":
            all_starting_points.append(str(i) + "," + str(j))
        if matrix[i][j] == "9":
            all_finish_points.append(str(i) + "," + str(j))
        build_graph(graph, matrix, i, j)


g = Graph(graph)
score = 0
for starting_point in all_starting_points:
    distances = g.shortest_distances(starting_point)
    distances_to_finish = {}
    for finish_point in all_finish_points:
        if distances[finish_point] != float("inf") and distances[finish_point] == 9:
            distances_to_finish[finish_point] = distances[finish_point]
    score += len(distances_to_finish)

print(score)