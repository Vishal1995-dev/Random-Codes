class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour=hour%12
        h=hour*30+(minutes*.5)
        m=minutes*6
        low=min(h,m)
        high=max(h,m)
        return min(high-low,360-high+low)
