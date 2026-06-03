# Завдання 5. Візуалізація обходу бінарного дерева
# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python,
# яка візуалізує обходи дерева: у глибину та в ширину.
# Кольори вузлів — від темних до світлих (#0a2463 → #1296F0). Стек і черга, без рекурсії.

from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

from task4 import Node, add_edges, build_tree_from_heap


DEFAULT_COLOR = "#D3D3D3"
DARK_COLOR = "#0a2463"
LIGHT_COLOR = "#1296F0"


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def generate_visit_colors(count: int, dark: str = DARK_COLOR, light: str = LIGHT_COLOR) -> list[str]:
    """Градієнт унікальних кольорів від темного до світлого для порядку обходу."""
    if count <= 0:
        return []
    if count == 1:
        return [light]

    start = _hex_to_rgb(dark)
    end = _hex_to_rgb(light)
    colors: list[str] = []

    for i in range(count):
        t = i / (count - 1)
        rgb = tuple(int(start[j] + (end[j] - start[j]) * t) for j in range(3))
        colors.append(_rgb_to_hex(rgb))

    return colors


def reset_colors(node: Node | None, color: str = DEFAULT_COLOR) -> None:
    if node is None:
        return
    node.color = color

    reset_colors(node.left, color)
    reset_colors(node.right, color)


def count_nodes(node: Node | None) -> int:
    if node is None:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


def dfs_with_stack(root: Node | None) -> list[Node]:
    if root is None:
        return []

    order: list[Node] = []
    stack: list[Node] = [root]

    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_with_queue(root: Node | None) -> list[Node]:
    if root is None:
        return []

    order: list[Node] = []
    queue: deque[Node] = deque([root])

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def _draw_on_axes(root: Node, ax, title: str) -> None:
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    ax.clear()
    ax.set_title(title)
    nx.draw(
        tree,
        pos=pos,
        ax=ax,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        with_labels=True,
    )


def visualize_traversal(
    root: Node,
    traversal_name: str,
    visit_order: list[Node],
    pause_sec: float = 0.8,
) -> None:
    reset_colors(root)
    palette = generate_visit_colors(len(visit_order))

    _fig, ax = plt.subplots(figsize=(9, 6))
    _draw_on_axes(root, ax, f"{traversal_name}: початковий стан")
    plt.pause(pause_sec)

    for step, node in enumerate(visit_order, start=1):
        node.color = palette[step - 1]
        _draw_on_axes(
            root,
            ax,
            f"{traversal_name}: крок {step}/{len(visit_order)} — вузол {node.val}",
        )
        plt.pause(pause_sec)

    plt.show()


def build_sample_tree() -> Node:
    """Дерево для демонстрації (як у прикладі з завдання 4)."""
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


def build_tree_from_heap_copy(heap: list) -> Node | None:
    """Окреме дерево з купи (нові id вузлів для чистої візуалізації)."""
    return build_tree_from_heap(heap)


if __name__ == "__main__":
    print("DFS (стек), pre-order:")
    tree_dfs = build_sample_tree()
    dfs_order = dfs_with_stack(tree_dfs)
    print(" → ".join(str(n.val) for n in dfs_order))
    visualize_traversal(tree_dfs, "Обхід у глибину (DFS)", dfs_order)

    print("\nBFS (черга):")
    tree_bfs = build_sample_tree()
    bfs_order = bfs_with_queue(tree_bfs)
    print(" → ".join(str(n.val) for n in bfs_order))
    visualize_traversal(tree_bfs, "Обхід у ширину (BFS)", bfs_order)
