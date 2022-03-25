class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ret=[]
        mini=2001
        d={}
        for i in range(len(list1)):
            d[list1[i]]=i
        for i in range(len(list2)):
            if(list2[i] in d):
                d[list2[i]]+=i
                if(d[list2[i]]<mini):
                    ret=[list2[i]]
                    mini=d[list2[i]]
                elif(d[list2[i]]==mini):
                    ret.append(list2[i])
        return ret
