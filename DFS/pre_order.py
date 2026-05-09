class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order(node, hasil=None):
    if hasil is None:
        hasil = []
    if node is not None:
        hasil.append(node.value)
        pre_order(node.left, hasil)
        pre_order(node.right, hasil)
    return hasil


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Pre-order :", pre_order(root))
