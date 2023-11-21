import heapq  #


class Graph:
    def __init__(self):
        self.nodes = (
            set()
        )  # menginisialisasi atribut 'nodes' dalam bentuk himpunan dengan set() agar tidak terjadi duplikasi node
        self.edges = {}  # menginisialisasi atribut 'edges' dalam bentuk dictionary
        # print("aku sudah dibuat -graph")

    def add_node(self, value):
        self.nodes.add(value)  # menambahkan nilai value ke dalam self.nodes
        self.edges[value] = []  # menambah nodes baru untuk dimasukan isi

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))


def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start, []))
    closed_set = set()
    print("state pertama:", open_set)
    print()

    while open_set:
        print("open_set: ", open_set)
        cost, current, path = heapq.heappop(open_set)

        print("current: ", current)
        print("cost: ", cost)
        print("path: ", path)
        print("closed_set: ", closed_set)
        print("===\n")

        # checking
        if current in closed_set:
            continue

        # buat tau path-nya
        path = path + [current]

        # kalo udah ketemu titik akhirnya
        if current == goal:
            return path, cost

        # menandakan node sudah di-visit
        closed_set.add(current)

        # ngecek tetangga
        for neighbor, distance in graph.edges[current]:
            if neighbor not in closed_set:
                heapq.heappush(open_set, (cost + distance, neighbor, path))

    return None


# Inisialisasi graf
city_map = Graph()
city_map.add_node("A")
city_map.add_node("B")
city_map.add_node("C")
city_map.add_node("D")
city_map.add_node("E")
city_map.add_node("F")
city_map.add_node("G")
city_map.add_node("H")
city_map.add_node("I")
city_map.add_node("J")

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
