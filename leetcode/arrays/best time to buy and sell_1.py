#%%
class Solution:
    def maxProfit(self, prices):

        p = 0
        max_p = 0
        first_p = [0]
        sec_p = [0]
        min_buy = prices[0]

        for i in range(len(prices)):

            if prices[i] < min_buy:
                min_buy = prices[i]
            p = prices[i] - min_buy

            if max(sec_p[i - 1], p) < max_p:
                sec_p.append(max(sec_p[i - 1], p))
            else:
                sec_p.append(sec_p[i - 1])

            if p > max_p:
                max_p = p
                first_p.append(p)

        s_idx = first_p.index(max_p)
        # return (max_p + max(sec_p[s_idx:]))
        return max_p


nums = [7,1,5,3,6,4]
s = Solution()
s.maxProfit(nums)

