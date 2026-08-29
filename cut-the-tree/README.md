# Cut the Tree

## A. Title of the Problem

Cut the Tree

## B. Problem Statement

Given a tree with `n` nodes, where each node has an associated integer
value, the objective is to remove one edge from the tree such that the
difference between the sums of the values in the two resulting
subtrees is minimized.

The tree is represented using edges connecting the nodes.

The objective is to determine the minimum possible difference between the
sums of the two parts after removing one edge.

## C. HackerRank Link

Cut the Tree - HackerRank-https://www.hackerrank.com/challenges/cut-the-tree/problem?utm_source=chatgpt.com

## D. GitHub Repository

This repository contains the Python implementation of the Cut the Tree
problem.

The complete source code is available in:

`cutthetree.py`

## E. Solution Steps / Algorithm

The problem is solved using Depth-First Search (DFS).

### Steps

1. Read the values of all the nodes.
2. Create an adjacency list to represent the tree.
3. Calculate the total sum of all node values.
4. Create a visited array to keep track of visited nodes.
5. Start DFS from the first node.
6. During DFS, calculate the sum of the current node and all nodes in
   its subtree.
7. Treat each subtree as one possible part after cutting an edge.
8. Calculate the sum of the remaining part using:
   `total_sum - current_sum`
9. Calculate the difference between the two parts.
10. Keep track of the minimum difference found.
11. Continue DFS until all possible subtrees are considered.
12. Return the minimum difference.

### Complexity

* Time Complexity: O(n)
* Space Complexity: O(n)

## F. Code Developed

The solution was implemented in Python using Depth-First Search (DFS).

The complete code is available in:

`cutthetree.py`

## G. HackerRank Test Case

The solution was tested on HackerRank.

A screenshot showing the successful HackerRank submission/test cases
is included in the assignment report.

## H. Observation

The problem was successfully solved using Depth-First Search (DFS).
DFS calculates the sum of each subtree, allowing every possible edge
cut to be considered.

The minimum difference between the two resulting parts is calculated
using the subtree sum and the total tree sum. The algorithm efficiently
finds the optimal edge to remove.

