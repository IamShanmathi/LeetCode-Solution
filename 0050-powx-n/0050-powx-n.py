class Solution:

  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1.0

    # Store whether power was originally negative
    is_negative = n < 0
    N = abs(n)

    res = 1.0
    current_product = x

    while N > 0:
      if N % 2 == 1:
        res *= current_product
      current_product *= current_product
      N //= 2

    return 1 / res if is_negative else res