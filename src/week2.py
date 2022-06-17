class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = []
        for a in s:
            if(dict[a] is not None):
                dict[a]+=1
            else:
                dict[a] = 0