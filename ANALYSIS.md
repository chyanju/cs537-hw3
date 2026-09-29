# HW3 Written Analysis (graded by a TA, 24 points)

Write your answers under each question. Short answers are fine: the reasoning is what counts, and it should match your own code.

## Q1. Complexity (6 points)

Let n be the number of nodes and h the height. Give the running time and the extra space (not counting the returned result, but counting the recursion stack) of **your** implementation.

| Function | Time | Space | Reason |
|---|---|---|---|
| `inorder` | | | |
| `bst_insert` | | | |
| `is_valid_bst` | | | |

## Q2. Why is your `is_valid_bst` correct? (6 points)

What exactly does your code check at each node, and why does that guarantee that every value in a node's left subtree is smaller and every value in its right subtree is larger?

## Q3. Very deep trees (6 points)

Suppose the tree is a chain of 100,000 nodes. What happens when your `height` runs on it, and why? How would you change `height` so that it works at any depth?

## Q4. Your own tests (6 points)

Give three tests that are not in `test_tree.py`, each aimed at a different mistake someone could make.

| Function | Tree (level-order) | Other args | Expected | Mistake it would catch |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
