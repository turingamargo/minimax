from __future__ import annotations

import random


class MiniMaxNode:
    left_node: MiniMaxNode | None
    right_node: MiniMaxNode | None
    value: int | None

    def __init__(self, value: int | None = None, left_node: MiniMaxNode | None = None,
                 right_node: MiniMaxNode | None = None) -> None:
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self) -> str:
        return str(self.value)


class MiniMaxTree:
    root: MiniMaxNode
    leaves: [int]

    @staticmethod
    def is_power_of_two(n):
        return (n & (n - 1) == 0) and n != 0

    def __init__(self, number_of_children: int) -> None:
        if not MiniMaxTree.is_power_of_two(number_of_children):
            raise ValueError(f"Number of children is not a power of two")

        self.leaves = random.sample(range(number_of_children), number_of_children)
        nodes = [MiniMaxNode(value) for value in self.leaves]

        while len(nodes) != 1:
            new_nodes = []
            for _ in range(len(nodes) // 2):
                child_1 = nodes.pop(0)
                child_2 = nodes.pop(0)
                parent = MiniMaxNode(left_node=child_1, right_node=child_2)
                new_nodes.append(parent)

            nodes = new_nodes

        self.root = nodes[0]


def minimax_recursive_solver(root: MiniMaxNode, maximize: bool):
    left_node = root.left_node
    right_node = root.right_node

    if left_node.value is not None and right_node.value is not None:
        if maximize:
            return left_node.value if left_node.value >= right_node.value else right_node.value
        else:
            return left_node.value if left_node.value <= right_node.value else right_node.value

    if maximize:
        return max(
            minimax_recursive_solver(root=root.left_node, maximize=False),
            minimax_recursive_solver(root=root.right_node, maximize=False)
        )
    else:
        return min(
            minimax_recursive_solver(root=root.left_node, maximize=True),
            minimax_recursive_solver(root=root.right_node, maximize=True)
        )
