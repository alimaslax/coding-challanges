# =============================================================================
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# class Solution(object):
#     def maxProfit(self, prices):
#         l,r = 0,1
#         maxim = 0
#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r]-prices[l]
#                 maxim = max(maxim,profit)
#             else:
#                 l = r
#             r += 1
#         return maxim
#
#
#
# solution = Solution
# prices = [1,2,4,2,5,7,2,4,9,0,9]
# print(solution.maxProfit(solution,prices));

# =============================================================================
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         char = set()
#         l = 0
#         ans = 0
#         for r in range(0,len(s)-1):
#             if s[r] in char:
#                 ans = max(ans,r-l+1)
#                 char = set()
#                 l = r
#             char.add(s[r])
#         return ans
#     def lengthOfLongestSubstring2(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0
#
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res
#
# solution = Solution
# s = "pwwkew"
# s2 = "abcabcbb"
# s3 = "bbbbb"
# s4 = ""
# print(solution.lengthOfLongestSubstring2(solution, s));

# =============================================================================
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Review HARD
# class Solution(object):
#     def characterReplacement(self, s, k):
#         l = 0;
#         count = 0
#         chrMax = 0
#         tmp = ""
#         for r in range(0,len(s)):
#             if s[l] == s[r]:
#                 count+=1
#             else:
#                 if(count > chrMax):
#                     tmp = s[l:r]
#                 chrMax = max(chrMax,count)
#                 count = 0
#                 l = r
#         return chrMax
#
#
# solution = Solution
# s = "ABBB"
# k = 2
# print(solution.characterReplacement(solution, s,k));

# =============================================================================
# https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        perms = set()
        if (len(s1) == 1):
            return s1 in s2
        for l in range(0,len(s1)-1):
            for r in range(1,len(s1)):
                s1 = s1[l] + s1[r:]
                perms.add(s1)
        for key in perms:
            if(key in s2):
                return True
        return False


solution = Solution
s1 = "b"
s2 = "abc"
print(solution.checkInclusion(solution, s1,s2));