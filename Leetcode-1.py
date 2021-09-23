for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target and not(i==j)):
                    return i,j
