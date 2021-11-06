class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        one=students.count(1)
        zero=students.count(0)
        
        for i in range(len(sandwiches)):
            if(sandwiches[i]==0):
                if(zero>0):
                    zero-=1
                else:
                    return len(sandwiches)-i
            else:
                if(one>0):
                    one-=1
                else:
                    return len(sandwiches)-i
        return 0
