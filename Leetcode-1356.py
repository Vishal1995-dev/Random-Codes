class Solution(object):
    def sortByBits(self, A):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda a: [bin(a).count('1'), a])
