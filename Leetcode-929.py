class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen=[]
        for i in emails:
            l=len(i)
            j=0
            s=""
            flag=0
            while(j<l):
                if(flag==0):
                    if(i[j]!='.'):
                        if(i[j]!='+'):
                            s+=i[j]
                            j+=1
                        else:
                            while(i[j]!='@'):
                                j+=1
                            s+='@'
                            j+=1
                            flag=1
                        if(i[j]=='@'):
                            while(i[j]!='@'):
                                j+=1
                            s+='@'
                            j+=1
                            flag=1
                    else:
                        j+=1
                else:
                    s+=i[j]
                    j+=1
            if(s not in seen):
                seen.append(s)
        return len(seen)
