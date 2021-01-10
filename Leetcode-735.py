class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        flag=1
        for i in range(len(asteroids)-1,0,-1):
            if(asteroids[i]<0 and asteroids[i-1]>0):
                flag=0
                if(abs(asteroids[i])<abs(asteroids[i-1])):
                    asteroids.pop(i)
                elif(abs(asteroids[i])>abs(asteroids[i-1])):
                    asteroids.pop(i-1)
                    break
                else:
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    break
        if(flag==0):
            return self.asteroidCollision(asteroids)
        return asteroids
