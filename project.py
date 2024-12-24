# Heap Sort Implementation
class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def sort(self):
        n = len(self.arr)

        # Build Max Heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)

        return self.arr


# Kruskal's Algorithm Implementation
class KruskalMST:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []  # To store the resulting MST
        i, e = 0, 0  # Index variables for sorted edges and result[]

        # Sort edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        # Initialize parent and rank arrays
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


# Example Usage for HeapSort
arr = [12, 7, 9, 3, 15, 1]
hs = HeapSort(arr)
sorted_arr = hs.sort()
print("Sorted Array using Heap Sort:", sorted_arr)

# Example Usage for Kruskal's Algorithm
graph = KruskalMST(5)
graph.add_edge(0, 1, 8)
graph.add_edge(0, 2, 12)
graph.add_edge(1, 3, 10)
graph.add_edge(1, 4, 6)
graph.add_edge(3, 4, 7)

mst = graph.kruskal()
print("Minimum Spanning Tree (MST):", mst)
