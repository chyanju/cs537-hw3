# CS537 HW3: Binary Tree Basics

1. Implement the 10 functions in `tree.py` (see each docstring).
2. Answer the four questions in `ANALYSIS.md`.

## Grading (100 points)

| Part | Points | How |
|---|---|---|
| A. Automated tests | 70 | 70 hidden tests, 1 point each |
| B. TA review | 30 | A TA reads `tree.py` (code quality, 6) and `ANALYSIS.md` (24) |

### Part A: what is tested

| Level | Functions | Tests |
|---|---|---|
| Basic | `preorder` `inorder` `postorder` `count_nodes` | 28 |
| Intermediate | `height` `count_leaves` `level_order` | 21 |
| Challenge | `bst_search_path` `bst_insert` `is_valid_bst` | 21 |

Each function has 7 tests:

| Metric | Tests | What it covers |
|---|---|---|
| typical | 2 | ordinary trees |
| edge | 2 | empty tree, single node, ... |
| tricky | 2 | nodes with one child, zero/negative/duplicate values, values not in the tree, ... |
| large | 1 | a few hundred nodes |

Only return values are checked, not speed. Each test has a 2-second limit, only to catch infinite loops.

### Part B: what the TA looks for

- **Code quality:** clear names, clean base cases, no leftover debug code, no needless work.
- **`ANALYSIS.md`:** complexity, a correctness argument, very deep trees, and three tests of your own. The TA grades your reasoning, so answer in your own words and about your own code.

## Tree notation

Trees in tests and docstrings are level-order lists, with `None` for a missing child. For example, `[1, 2, 3, 4, 5]` and `[1, None, 2]`:

```
      1        1
     / \        \
    2   3        2
   / \
  4   5
```

## Self-check

```bash
python3 test_tree.py
```

This runs the 30 public tests, which are also part of the 70 hidden tests.
