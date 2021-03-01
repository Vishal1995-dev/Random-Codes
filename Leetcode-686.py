class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
