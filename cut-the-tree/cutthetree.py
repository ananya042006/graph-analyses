#!/usr/bin/env python3

import sys
sys.setrecursionlimit(10**6)

def cutTheTree(data, edges):
    n = len(data)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    total_sum = sum(data)
    visited = [False] * n
    min_diff = float('inf')

    def dfs(node):
        nonlocal min_diff
        visited[node] = True
        current_sum = data[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                current_sum += dfs(neighbor)
        diff = abs(total_sum - 2 * current_sum)
        min_diff = min(min_diff, diff)
        return current_sum

    dfs(0)
    return min_diff


def main():
    # Read input
    n = int(sys.stdin.readline().strip())
    data = list(map(int, sys.stdin.readline().strip().split()))
    edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n - 1)]
    print(cutTheTree(data, edges))


if __name__ == "__main__":
    # If you want to run with redirected input (e.g. < input.txt), just call main()
    if sys.stdin.isatty():
        # Interactive mode: run a quick test harness
        sample_input = """6
100 200 100 500 100 600
1 2
2 3
2 5
4 5
5 6
"""
        from io import StringIO
        sys.stdin = StringIO(sample_input)
        main()
    else:
        main()
