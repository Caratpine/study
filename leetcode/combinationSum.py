class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []

        def backtracing(nums, i, size, path, res, target):
            if target == 0:
                res.append(path[:])
                return
            for idx in range(i, size):
                r = target - nums[idx]
                if r < 0:
                    break
                path.append(nums[idx])
                backtracing(nums, idx, size, path, res, r)
                path.pop()

        backtracing(candidates, 0, size, path, res, target)
        return res
