class Solution(object):
    def distanceBetweenBusStops(self, d, s, de):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if(s>de):
            s,de=de,s
        return min(sum(d[s:de]),sum(d)-sum(d[s:de]))
