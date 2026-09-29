"""CS537 HW3: binary tree basics. This is the only code file you need to edit.

An empty tree is None. Docstrings write trees as level-order lists (see README), e.g. [1, 2, 3, 4, 5].
"""


class TreeNode:  # do not modify
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== Basic =====

def preorder(root):
    """Preorder traversal (root, left, right) as a list of values.  [1, 2, 3, 4, 5] -> [1, 2, 4, 5, 3]"""
    raise NotImplementedError


def inorder(root):
    """Inorder traversal (left, root, right).  [1, 2, 3, 4, 5] -> [4, 2, 5, 1, 3]"""
    raise NotImplementedError


def postorder(root):
    """Postorder traversal (left, right, root).  [1, 2, 3, 4, 5] -> [4, 5, 2, 3, 1]"""
    raise NotImplementedError


def count_nodes(root):
    """Number of nodes.  [1, 2, 3, 4, 5] -> 5"""
    raise NotImplementedError


# ===== Intermediate =====

def height(root):
    """Number of nodes on the longest root-to-leaf path; 0 for an empty tree.  [1, 2, 3, 4, 5] -> 3"""
    raise NotImplementedError


def count_leaves(root):
    """Number of leaves (nodes with no children).  [1, 2, 3, 4, 5] -> 3"""
    raise NotImplementedError


def level_order(root):
    """Values level by level, left to right, one list per level.  [1, 2, 3, 4, 5] -> [[1], [2, 3], [4, 5]]"""
    raise NotImplementedError


# ===== Challenge: binary search trees (left subtree < node < right subtree) =====

def bst_search_path(root, val):
    r"""Search for val from the root using the BST rule and return the values visited:
    up to and including the matching node, or until the search falls off the tree.

    Example tree [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]:
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \    /
         4   7  13
    search 7 -> [8, 3, 6, 7]; search 5 -> [8, 3, 6, 4]
    """
    raise NotImplementedError


def bst_insert(root, val):
    """Insert val as a new leaf and return the root; if val is already present, leave the tree unchanged.
    [4, 2, 7, 1, 3] insert 5 -> [4, 2, 7, 1, 3, 5]
    """
    raise NotImplementedError


def is_valid_bst(root):
    """True if every node is greater than all values in its left subtree and less than all values
    in its right subtree (so no duplicates). An empty tree is valid.  [2, 1, 3] -> True; [2, 3, 1] -> False
    """
    raise NotImplementedError
