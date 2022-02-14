class MyStack(object):

    def __init__(self):
        self.a=[]        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.a.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.a)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
