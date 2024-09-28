from typing import List
#LEETCODE
#this section is for leetcode problems, solutions, and related info

#   Two-Sum + generic understanding of process
#goal: Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
class Solution:# class definition
    #def(function), twosum(name),
    #self is a reference to the instance of the class itself; required
    #num and target are input for list of numbers and target number
    #->List[int] this is the what the method will return as an output, a list of numbers
    def twoSum(self, nums: List[int], target: int) -> List[int]:# method definition
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    #print(nums[i], nums[j])
                    #print(i,j)
                    return [i,j]
        return []

solution = Solution()# instance of solution class
result = solution.twoSum([3,3], 6)# accessing instance method
print(result)
