from __future__ import annotations


class MiniMaxNode:
    left_node: MiniMaxNode | None
    right_node: MiniMaxNode | None
    value: int | None

    def __init__(self, value=None, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return str(self.value)


class MiniMaxTree:
    root: MiniMaxNode
    values: [int]

    @staticmethod
    def is_power_of_two(n):
        return (n & (n - 1) == 0) and n != 0

    def __init__(self, values):
        if not MiniMaxTree.is_power_of_two(len(values)):
            raise ValueError(f"Number of children is not a power of two")

        self.values = values
        nodes = [MiniMaxNode(value) for value in self.values]

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
            minimax_recursive_solver(root=left_node, maximize=False),
            minimax_recursive_solver(root=right_node, maximize=False)
        )
    else:
        return min(
            minimax_recursive_solver(root=left_node, maximize=True),
            minimax_recursive_solver(root=right_node, maximize=True)
        )


if __name__ == "__main__":
    test_values = [7, 5, 3, 2, 4, 1, 0, 6]
    tree = MiniMaxTree(values=test_values)
    max_value = minimax_recursive_solver(root=tree.root, maximize=True)
    print(max_value)
