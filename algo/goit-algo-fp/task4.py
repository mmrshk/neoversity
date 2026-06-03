# Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
# 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.

import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_tree_from_heap(heap: list, index: int = 0, color: str = "skyblue") -> Node | None:
    if index >= len(heap):
        return None

    node = Node(heap[index], color=color)
    node.left = build_tree_from_heap(heap, 2 * index + 1, color)
    node.right = build_tree_from_heap(heap, 2 * index + 2, color)
    return node


def draw_heap(heap: list, color: str = "skyblue") -> None:
    if not heap:
        print("Купа порожня")
        return
    root = build_tree_from_heap(heap, color=color)
    draw_tree(root)

if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3]
    draw_heap(heap)


# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# python task4.py