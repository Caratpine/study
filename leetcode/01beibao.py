class Solution:
    def __init__(self):
        self.max = -1

    def beibao(self, weight, w):
        def helper(i, cw):
            if cw == w or i == len(weight):
                if cw > self.max:
                    self.max = cw
                return
            helper(i + 1, cw);
            if (cw + weight[i] <= w):
                helper(i + 1, cw + weight[i])
        helper(0, 0)
        return self.max


if __name__ == '__main__':
    res = Solution().beibao([2, 2, 4, 6, 3], 9)
    print(res)
