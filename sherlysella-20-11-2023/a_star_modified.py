import heapq
import math
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        # menginisialisasi atribut 'nodes' dalam bentuk himpunan dengan set() agar tidak terjadi duplikasi node
        self.nodes = set()
        self.edges = {}  # menginisialisasi atribut 'edges' dalam bentuk dictionary
        self.coordinates = {}

    def add_node(self, value, coordinates):
        self.nodes.add(value)  # menambahkan nilai value ke dalam self.nodes
        self.edges[value] = []  # menambah nodes baru untuk dimasukan isi
        self.coordinates[
            value
        ] = coordinates  # menyimpan koordinat untuk menghitung euclidean distance

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))


def euclidean_distance(graph, node1, node2):
    # This function assumes that the coordinates are stored in a tuple or list
    # For example: coordinates['A'] = (x1, y1)
    x1, y1 = graph.coordinates[node1]
    x2, y2 = graph.coordinates[node2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + euclidean_distance(graph, start, goal), start, []))
    closed_set = set()

    while open_set:
        cost, current, path = heapq.heappop(open_set)

        if current in closed_set:
            continue

        path = path + [current]

        if current == goal:
            return path, cost - euclidean_distance(graph, current, goal)

        closed_set.add(current)

        for neighbor, distance in graph.edges[current]:
            if neighbor not in closed_set:
                heapq.heappush(
                    open_set,
                    (
                        cost + distance + euclidean_distance(graph, neighbor, goal),
                        neighbor,
                        path,
                    ),
                )

    return None


def plot_nodes(city_map):
    fig, ax = plt.subplots()

    # Get the coordinates of the nodes
    x_coords = [coords[0] for coords in city_map.coordinates.values()]
    y_coords = [coords[1] for coords in city_map.coordinates.values()]

    # Plot the nodes
    ax.scatter(x_coords, y_coords)

    # Annotate the nodes with their names
    for node, coords in city_map.coordinates.items():
        ax.annotate(node, (coords[0], coords[1]))

    plt.show()


# Inisialisasi graf
city_map = Graph()
city_map.add_node("A", (2, 3))
city_map.add_node("B", (3, 2))
city_map.add_node("C", (10, 6))
city_map.add_node("D", (7, 3))
city_map.add_node("E", (5, 6))
city_map.add_node("F", (5, 2))
city_map.add_node("G", (8, 5))
city_map.add_node("H", (8, 9))
city_map.add_node("I", (3, 4))
city_map.add_node("J", (10, 5))

city_map.add_edge("A", "B", 37)
city_map.add_edge("A", "I", 48)
city_map.add_edge("B", "F", 68)
city_map.add_edge("C", "G", 29)
city_map.add_edge("C", "H", 42)
city_map.add_edge("C", "J", 28)
city_map.add_edge("D", "E", 69)
city_map.add_edge("D", "F", 73)
city_map.add_edge("D", "J", 42)
city_map.add_edge("E", "H", 106)
city_map.add_edge("E", "I", 80)
city_map.add_edge("F", "I", 43)
city_map.add_edge("G", "J", 27)

# plot graph
# plot_nodes(city_map)

# Meminta input dari pengguna
start = input("Masukkan lokasi awal: ").upper()
goal = input("Masukkan lokasi tujuan: ").upper()

# Menjalankan algoritma A*
path, cost = astar(city_map, start, goal)

# Menampilkan hasil
if path:
    print(f"Rute terpendek dari {start} ke {goal}: {path}")
    print(f"Jarak yang ditempuh: {cost} km")
else:
    print(f"Tidak ada rute dari {start} ke {goal}.")
