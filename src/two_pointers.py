# =============================================================================
# https://leetcode.com/problems/valid-palindrome/
# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         s = re.sub(r'[^a-zA-Z0-9]', '', s)
#         tmp = ''.join(reversed(s))
#         return s.lower() == tmp.lower()
#
# solution = Solution
# s = "A man, a plan, a canal: Panama"
# print(solution.isPalindrome(solution,s));

# =============================================================================
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# class Solution(object):
#     def twoSum(self, numbers, target):
#         ls = 0
#         rs = len(numbers)-1
#         while ls != rs:
#             if numbers[ls] + numbers[rs] == target:
#                 return [ls+1,rs+1]
#             if numbers[ls] + numbers[rs] > target:
#                 rs = rs - 1
#             else:
#                 ls = ls + 1
#
# solution = Solution
# numbers = [2,3,4,5,6,7]
# target = 9
# print(solution.twoSum(solution,numbers,target));

# =============================================================================
# https://leetcode.com/problems/3sum/
# HARD :: edge cases
# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         i = 0;
#         k = len(nums) - 1
#         j = 1;
#         list = []
#         while i + 1 < k:
#             if nums[i] + nums[j] + nums[k] == 0:
#                 list.append([nums[i], nums[j], nums[k]])
#                 i = i + 1
#                 j = i + 1
#             if nums[i] + nums[j] + nums[k] > 0:
#                 k = k - 1
#                 j = k - 1
#             if nums[i] + nums[j] + nums[k] < 0:
#                 i = i + 1
#                 j = i + 1
#         return list
#
#
# solution = Solution
# nums = [-2,0,1,1,2]
# print(solution.threeSum(solution, nums));

# =============================================================================
# https://leetcode.com/problems/container-with-most-water/
# HARD :: understanding the problem

class Solution(object):
    def maxArea(self, height):
        area = 0
        for l in range (0, len(height)-1):
            for r in range (len(height)-1,l,-1):
                area = max(area, min(height[l],height[r])*(r-l))
                if(height[l]<=r):
                    l += 1
        return area

solution = Solution
height = [1,8,6,2,5,4,8,3,7]
height2 = [4,3,2,1,4]
height3 = [1,2]
height4 = [0,2]
height5 = [1,2,4,3]
height6 = [18,17,6]
print(solution.maxArea(solution, height6));