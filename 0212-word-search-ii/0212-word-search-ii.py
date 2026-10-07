class TrieNode:

  def __init__(self):
    self.children = {}
    self.word = None  # Stores the complete word at leaf nodes


class Solution:

  def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
    # 1. Build the Trie
    root = TrieNode()
    for word in words:
      node = root
      for char in word:
        if char not in node.children:
          node.children[char] = TrieNode()
        node = node.children[char]
      node.word = word  # Store full word at the end node

    ROWS, COLS = len(board), len(board[0])
    result = []

    # 2. DFS Backtracking Function
    def dfs(r, c, parent_node):
      char = board[r][c]
      curr_node = parent_node.children[char]

      # Check if a word is found
      if curr_node.word:
        result.append(curr_node.word)
        curr_node.word = None  # Avoid duplicate additions

      # Mark visited
      board[r][c] = '#'

      # Explore 4-directional neighbors
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < ROWS
            and 0 <= nc < COLS
            and board[nr][nc] in curr_node.children
        ):
          dfs(nr, nc, curr_node)

      # Backtrack: Restore original character
      board[r][c] = char

      # Optimization: Prune leaf nodes with no children
      if not curr_node.children:
        parent_node.children.pop(char)

    # 3. Start DFS from each cell
    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] in root.children:
          dfs(r, c, root)

    return result