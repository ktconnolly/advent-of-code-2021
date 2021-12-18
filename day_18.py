import ast
import itertools
import math


def read_input():
    with open("inputs/day_18.txt") as file:
        return [ast.literal_eval(line.strip()) for line in file]


class Node:
    def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(left={self.left}, right={self.right})"


def list_to_tree(lst, parent=None):
    left, right = lst

    if isinstance(left, int) and isinstance(right, int):
        node = Node(parent)
        node.left = left
        node.right = right
        return node

    if isinstance(left, int):
        node = Node(parent)
        node.left = left
        node.right = list_to_tree(right, node)
        return node

    if isinstance(right, int):
        node = Node(parent)
        node.left = list_to_tree(left, node)
        node.right = right
        return node

    node = Node(parent)
    node.left = list_to_tree(left, node)
    node.right = list_to_tree(right, node)
    return node


def tree_to_list(node):
    return node if isinstance(node, int) else [tree_to_list(node.left), tree_to_list(node.right)]


def add_to_left(node, amount):
    if isinstance(node.left, int):
        node.left += amount
        return

    while node.parent.left is node:
        node = node.parent
        if not node.parent:
            return

    node = node.parent
    if isinstance(node.left, int):
        node.left += amount
        return

    node = node.left
    while not isinstance(node.right, int):
        node = node.right
    node.right += amount


def add_to_right(node, amount):
    while node.parent.right is node:
        node = node.parent
        if not node.parent:
            return

    if isinstance(node.parent.right, int):
        node.parent.right += amount
        return

    node = node.parent.right
    while not isinstance(node.left, int):
        node = node.left
    node.left += amount


def explode(node, depth=0):
    left = node.left
    right = node.right

    if depth == 4:
        add_to_left(node.parent, left)
        add_to_right(node, right)

        if node is node.parent.left:
            node.parent.left = 0
        else:
            node.parent.right = 0

        return node, True

    if isinstance(left, Node):
        explode(left, depth + 1)
    if isinstance(right, Node):
        explode(right, depth + 1)

    return node, False


def split_number(n):
    return math.floor(n / 2), math.ceil(n / 2)


def split_left(node):
    if isinstance(node.left, int) and node.left >= 10:
        n1, n2 = split_number(node.left)
        node.left = Node(parent=node, left=n1, right=n2)
        return True

    return isinstance(node.left, Node) and split(node.left)


def split_right(node):
    if isinstance(node.right, int) and node.right >= 10:
        n1, n2 = split_number(node.right)
        node.right = Node(parent=node, left=n1, right=n2)
        return True

    return isinstance(node.right, Node) and split(node.right)


def split(node):
    return split_left(node) or split_right(node)


def reduce(node):
    while True:
        node, is_exploded = explode(node)
        if is_exploded:
            continue

        is_split = split(node)

        if not is_exploded and not is_split:
            return node


def get_magnitude(n):
    left, right = n.left, n.right
    if isinstance(left, Node):
        left = get_magnitude(left)
    if isinstance(right, Node):
        right = get_magnitude(right)
    return 3 * left + 2 * right


def part_one():
    lines = read_input()
    l1 = lines[0]
    res = None
    for l2 in lines[1:]:
        l1 = list_to_tree([l1, l2])
        res = reduce(l1)
        l1 = tree_to_list(res)

    return get_magnitude(res)


def part_two():
    lines = read_input()
    max_magnitude = 0
    for l in itertools.permutations(lines, 2):
        l = list_to_tree(l)
        res = reduce(l)
        max_magnitude = max(get_magnitude(res), max_magnitude)

    return max_magnitude


assert part_one() == 3691
assert part_two() == 4756
