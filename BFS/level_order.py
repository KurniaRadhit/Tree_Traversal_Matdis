from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def level_order(root):
    hasil = []
    if root is None:
        return hasil

    antrian = deque([root])
    while antrian:
        node = antrian.popleft()
        hasil.append(node.value)
        if node.left:
            antrian.append(node.left)
        if node.right:
            antrian.append(node.right)
    return hasil


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Level-order :", level_order(root))
