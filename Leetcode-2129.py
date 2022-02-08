class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title=title.lower()
        a=title.split(" ")
        ret=""
        for i in a:
            if(len(i)<=2):
                ret+=i
            else:
                ret+=i[0].upper()+i[1:]
            ret+=" "
        return ret[:-1]
