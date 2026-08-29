# Journey to the Moon

## A. Title of the Problem

Journey to the Moon

## B. Problem Statement

Given `n` astronauts and a list of pairs representing astronauts who
belong to the same country, the objective is to determine the number of
possible pairs of astronauts who belong to different countries.

Astronauts connected directly or indirectly through the given pairs are
considered to belong to the same country.

The objective is to count the total number of valid pairs of astronauts
that can be selected from different countries.

## C. HackerRank Link

Journey to the Moon - https://www.hackerrank.com/challenges/journey-to-the-moon/problem?utm_source=chatgpt.com

## D. GitHub Repository

This repository contains the Python implementation of the Journey to the
Moon problem.

The complete source code is available in:

`moon.py`

## E. Solution Steps / Algorithm

The problem is solved using Depth-First Search (DFS) and connected
components.

### Steps

1. Read the number of astronauts and the number of astronaut pairs.
2. Create an adjacency list to represent the connections between
   astronauts.
3. Create a visited array to keep track of visited astronauts.
4. Start DFS from every unvisited astronaut.
5. During DFS, find all astronauts connected to the current astronaut.
6. Calculate the size of each connected component.
7. Store the sizes of all connected components in `country_sizes`.
8. Calculate the number of valid pairs between astronauts belonging to
   different countries.
9. For each country, multiply its size by the number of astronauts
   remaining in other countries.
10. Add these values to obtain the total number of valid pairs.
11. Return the total number of valid astronaut pairs.

### Complexity

* Time Complexity: O(n + p)
* Space Complexity: O(n + p)

where `n` is the number of astronauts and `p` is the number of astronaut
pairs.

## F. Code Developed

The solution was implemented in Python using Depth-First Search (DFS)
and connected components.

The complete code is available in:

`moon.py`

## G. HackerRank Test Case

The solution was tested on HackerRank.

A screenshot showing the successful HackerRank submission/test cases
is included in the assignment report.

## H. Observation

The problem was successfully solved using Depth-First Search (DFS) to
identify connected components representing different countries.

After finding the size of each country, the number of possible pairs
between different countries is calculated. The approach efficiently
counts all valid astronaut pairs without counting duplicate pairs.

