import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key)


data = list(map(int, input().split()))


root = None
for key in data:
    root = insert(root, key)


postorder(root)
