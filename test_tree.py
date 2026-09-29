"""Public tests: python3 test_tree.py

These 30 tests are part of the 70 hidden tests. Each test is (metric, label, tree, other args..., expected).
"""
from collections import deque

import tree

BST = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]

CASES = {
    "preorder": [
        ("edge", "empty tree", [], []),
        ("edge", "single node", [1], [1]),
        ("typical", "example tree", [1, 2, 3, 4, 5], [1, 2, 4, 5, 3]),
    ],
    "inorder": [
        ("edge", "empty tree", [], []),
        ("edge", "single node", [1], [1]),
        ("typical", "example tree", [1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
    ],
    "postorder": [
        ("edge", "empty tree", [], []),
        ("edge", "single node", [1], [1]),
        ("typical", "example tree", [1, 2, 3, 4, 5], [4, 5, 2, 3, 1]),
    ],
    "count_nodes": [
        ("edge", "empty tree", [], 0),
        ("edge", "single node", [1], 1),
        ("typical", "example tree", [1, 2, 3, 4, 5], 5),
    ],
    "height": [
        ("edge", "empty tree", [], 0),
        ("edge", "single node", [1], 1),
        ("typical", "example tree", [1, 2, 3, 4, 5], 3),
    ],
    "count_leaves": [
        ("edge", "empty tree", [], 0),
        ("edge", "single node", [1], 1),
        ("typical", "example tree", [1, 2, 3, 4, 5], 3),
    ],
    "level_order": [
        ("edge", "empty tree", [], []),
        ("edge", "single node", [1], [[1]]),
        ("typical", "example tree", [1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
    ],
    "bst_search_path": [
        ("edge", "empty tree", [], 5, []),
        ("typical", "found in left subtree", BST, 7, [8, 3, 6, 7]),
        ("tricky", "not found, stops mid-tree", BST, 5, [8, 3, 6, 4]),
    ],
    "bst_insert": [
        ("edge", "insert into empty tree", [], 5, [5]),
        ("edge", "single node, insert left", [5], 3, [5, 3]),
        ("typical", "example", [4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
    ],
    "is_valid_bst": [
        ("edge", "empty tree", [], True),
        ("typical", "valid BST", BST, True),
        ("typical", "left child larger than root", [2, 3, 1], False),
    ],
}


def build(values):
    """Level-order list -> TreeNode (None for an empty tree)"""
    if not values:
        return None
    items = iter(values)
    root = tree.TreeNode(next(items))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left, right = next(items, None), next(items, None)
        if left is not None:
            node.left = tree.TreeNode(left)
            queue.append(node.left)
        if right is not None:
            node.right = tree.TreeNode(right)
            queue.append(node.right)
    return root


def to_list(root):
    """TreeNode -> level-order list, without trailing Nones"""
    values, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.extend([node.left, node.right])
    while values and values[-1] is None:
        values.pop()
    return values


def main():
    passed = total = 0
    for name, cases in CASES.items():
        ok, notes = 0, []
        for tag, label, values, *args, expected in cases:
            try:
                got = getattr(tree, name)(build(values), *args)
                if name == "bst_insert":
                    got = to_list(got)
            except NotImplementedError:
                notes = ["not implemented"]
                break
            except Exception as e:
                notes.append(f"✗ [{tag}] {label}: {type(e).__name__}: {e}")
                continue
            if got == expected:
                ok += 1
            else:
                notes.append(f"✗ [{tag}] {label}: expected {expected!r}, got {got!r}")
        passed += ok
        total += len(cases)
        print(f"{name:<16}{ok}/{len(cases)}")
        for note in notes:
            print("    " + note)
    print(f"\nPublic tests passed: {passed}/{total}")


if __name__ == "__main__":
    main()
