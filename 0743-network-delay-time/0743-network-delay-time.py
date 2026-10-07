from collections import defaultdict
import heapq


class Solution:

  def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
    # Build adjacency list
    adj = defaultdict(list)
    for u, v, w in times:
      adj[u].append((v, w))

    # Min-heap stores (time, node)
    min_heap = [(0, k)]
    visited = {}

    while min_heap:
      time, node = heapq.heappop(min_heap)

      if node in visited:
        continue

      visited[node] = time

      for neighbor, weight in adj[node]:
        if neighbor not in visited:
          heapq.heappush(min_heap, (time + weight, neighbor))

    return max(visited.values()) if len(visited) == n else -1
        