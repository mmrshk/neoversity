# Завдання 3. Дерева, алгоритм Дейкстри

# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу.
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення
# найкоротших шляхів від початкової вершини до всіх інших.

import heapq;

def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\\n")

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)];
    visited = set()

    while heap:
        dist_u, u = heapq.heappop(heap);

        if u in visited:
            continue
        visited.add(u)

        for neighbor, weight in graph[u].items():
            new_dist = dist_u + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    print_table(distances, visited)
    return distances

if __name__ == "__main__":
    # Приклад графа у вигляді словника
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    # Виклик функції для вершини A
    dijkstra(graph, 'A')

