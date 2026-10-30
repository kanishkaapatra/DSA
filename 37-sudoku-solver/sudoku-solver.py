
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Initialize row, column and box sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack(pos):
            if pos == len(empty):
                return True

            # Choose the empty cell with the fewest candidates
            best = pos
            best_candidates = None

            for i in range(pos, len(empty)):
                r, c = empty[i]
                box = (r // 3) * 3 + (c // 3)

                candidates = [
                    str(num) for num in range(1, 10)
                    if str(num) not in rows[r]
                    and str(num) not in cols[c]
                    and str(num) not in boxes[box]
                ]

                if best_candidates is None or len(candidates) < len(best_candidates):
                    best = i
                    best_candidates = candidates

                if len(best_candidates) == 0:
                    return False

                if len(best_candidates) == 1:
                    break

            # Swap the most constrained cell into current position
            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            box = (r // 3) * 3 + (c // 3)

            for num in best_candidates:
                board[r][c] = num

                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack(pos + 1):
                    return True

                # Undo the placement
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        backtrack(0)
