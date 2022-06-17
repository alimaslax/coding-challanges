# https://leetcode.com/problems/contains-duplicate/
# class Solution(object):
#     def containsDuplicate(self, nums):
#         d = {}
#         for x in nums:
#             if x in d:
#                 return False
#             d[x] = 1
#         return True
#
#
# nums = [1, 2 ,3, 4]
# solution = Solution
# print(solution.containsDuplicate(solution,nums));


# =============================================================================
# https://leetcode.com/problems/valid-anagram/
# class Solution(object):
#     def isAnagram(self, s, t):
#         s = ''.join(sorted(s))
#         t = ''.join(sorted(t))
#         if s == t:
#             return True
#         return False
#
# s = "abciii"
# t = "iiicba"
# solution = Solution
# print(solution.isAnagram(solution,s,t));

# =============================================================================
# https://leetcode.com/problems/two-sum/
# HARD ***
# sort has a runtime complexity of O(n*logn).
# class Solution(object):
#     def twoSum(self, nums, target):
#         size = len(nums)
#         for i in range(0,size-1):
#             for j in range(1,size):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]
#         return
#
# nums = [3,2,4]
# target = 6
# solution = Solution
# print(solution.twoSum(solution,nums,target));

# =============================================================================
# https://leetcode.com/problems/group-anagrams/
# class Solution(object):
#     def groupAnagrams(self, strs):
#         d = {}
#         empty = [[]]
#         for x in strs:
#             if x == "":
#                 empty[0].append("")
#                 continue
#             sorted_x = ''.join(sorted(x))
#             if sorted_x in d:
#                 d[sorted_x].append(x)
#             else:
#                 d[sorted_x] = [x]
#         anagrams = []
#         for x in d:
#             anagrams.append(d[x])
#         if empty[0] == []:
#             return anagrams
#         return empty + anagrams
#
# strs = [""]
# strs2 = ["bca","","abc", "ba","bab", "ab"]
# strs3 = ["eat","tea","tan","ate","nat","bat"]
# solution = Solution
# print(solution.groupAnagrams(solution,strs));

# =============================================================================
# https://leetcode.com/problems/top-k-frequent-elements/
# SOLUTION 1
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         nums.sort()
#         freq = [[] for i in range(len(nums) + 1)]
#         count = 1
#         d = {}
#         while len(nums) >= 1:
#             tmp = nums.pop(0)
#             if nums and tmp == nums[0]:
#                 count+=1
#             else:
#                 freq[count-1].append(tmp)
#                 count = 1
#         list = []
#         count = 0
#         for i in range(len(freq)-1,-1,-1):
#             if k <= 0:
#                 break;
#             for x in freq[i]:
#                 list.append(x)
#                 k = k - 1;
#         return list
#
# solution = Solution
# nums = [0,1,2,9,9,9,2,2,3]
# k = 4
# print(solution.topKFrequent(solution,nums,k));

# =============================================================================