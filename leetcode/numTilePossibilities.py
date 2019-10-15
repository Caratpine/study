# coding=utf-8


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking(tiles, idx, tmp, idx_tmp):
            ss = ''.join(tmp)
            if ss and ss not in results:
                results.append(ss)

            for idx, s in enumerate(tiles):
                if idx in idx_tmp:
                    continue
                tmp.append(s)
                idx_tmp.append(idx)
                backtracking(tiles, idx, tmp, idx_tmp)
                tmp.pop()
                idx_tmp.pop()
        results = []
        tmp = []
        idx_tmp = []
        backtracking(tiles, 0, tmp, idx_tmp)
        return len(results)
