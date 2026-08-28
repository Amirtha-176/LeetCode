class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        main_diag = set()
        second_diag = set()

        result = 0

        def backtracking(row: int):
            if row == n:
                nonlocal result
                result += 1

            for idx in range(n):
                md_idx, sd_idx = row - idx, row + idx

                if idx in columns or md_idx in main_diag or sd_idx in second_diag:
                    continue

                columns.add(idx)
                main_diag.add(md_idx)
                second_diag.add(sd_idx)

                backtracking(row + 1)

                second_diag.remove(sd_idx)
                main_diag.remove(md_idx)
                columns.remove(idx)

        backtracking(0)
        return result