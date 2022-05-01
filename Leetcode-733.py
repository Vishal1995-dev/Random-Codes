class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        a=[[0,1],[1,0],[0,-1],[-1,0]]
        m=len(image)
        n=len(image[0])
        val=image[sr][sc]
        if(image[sr][sc]==newColor):
            return image
        def fill(i,j):
            for p in a:
                new_i=i+p[0]
                new_j=j+p[1]
                if(new_i>=0 and new_j>=0 and new_i<m and new_j<n and val==image[new_i][new_j]):
                    image[new_i][new_j]=newColor
                    fill(new_i,new_j)
        fill(sr,sc)
        image[sr][sc]=newColor
        return image
