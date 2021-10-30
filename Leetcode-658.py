class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i=0
        if(arr[0]>=x):
            return arr[:k]
        i=len(arr)-1
        if(arr[i]<=x):
            return arr[len(arr)-k:]
        ret=[]
        for i in range(len(arr)-1):
            if(arr[i]==x):
                ret.append(arr[i])
                k-=1
                l=i-1
                m=i+1
                while(k>0):
                    a=9999999
                    b=9999999
                    if(l>=0):
                        a=arr[i]-arr[l]
                    if(m<len(arr)):
                        b=arr[m]-arr[i]
                    if(a<=b):
                        ret.append(arr[l])
                        l-=1
                    else:
                        ret.append(arr[m])
                        m+=1
                    k-=1
                ret.sort()
                return ret
            elif(arr[i]<x and arr[i+1]>x):
                l=i
                m=i+1
                while(k>0):
                    a=9999999
                    b=9999999
                    if(l>=0):
                        a=x-arr[l]
                    if(m<len(arr)):
                        b=arr[m]-x
                    if(a<=b):
                        ret.append(arr[l])
                        l-=1
                    else:
                        ret.append(arr[m])
                        m+=1
                    k-=1
                ret.sort()
                return ret
                
        
