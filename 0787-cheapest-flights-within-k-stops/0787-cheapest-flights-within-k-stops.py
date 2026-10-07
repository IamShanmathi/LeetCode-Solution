
class Solution:

  def findCheapestPrice(
      self, n: int, flights: list[list[int]], src: int, dst: int, k: int
  ) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    # Perform up to k + 1 iterations (k stops = k + 1 flights)
    for _ in range(k + 1):
      tmp_prices = prices.copy()

      for u, v, price in flights:
        if prices[u] == float("inf"):
          continue
        if prices[u] + price < tmp_prices[v]:
          tmp_prices[v] = prices[u] + price

      prices = tmp_prices

    return prices[dst] if prices[dst] != float("inf") else -1