class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        a=set()
        b=set()
        for i in paths:
            a.add(i[0])
            b.add(i[1])
        s=b-a
        for i in s:
            return i
