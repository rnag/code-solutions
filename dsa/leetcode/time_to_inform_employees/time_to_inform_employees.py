"""
The head of the company wants to inform all the company employees
of an urgent piece of news. He will inform his direct subordinates,
and they will inform their subordinates, and so on until all employees
know about the urgent news.

Return the number of minutes needed to inform all the employees about
the urgent news.

https://leetcode.com/problems/time-needed-to-inform-all-employees/

"""

from __future__ import annotations


__all__ = ['time_needed_to_inform_employees']


def time_needed_to_inform_employees(n: int, head_id: int, managers: list[int], inform_time: list[int]) -> int:
    adjacency_list = [[] for _ in range(n)]

    for e in range(n):
        manager = managers[e]

        if manager == -1:
            continue

        adjacency_list[manager].append(e)

    return dfs(head_id, adjacency_list, inform_time)


def dfs(start_id, adjacency_list, inform_time):
    max_time = 0

    subordinates = adjacency_list[start_id]

    if not subordinates:
        return max_time

    for e in subordinates:
        max_time = max(max_time, dfs(e, adjacency_list, inform_time))

    return max_time + inform_time[start_id]
