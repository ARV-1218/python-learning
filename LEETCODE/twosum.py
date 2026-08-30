class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        revisedList =[]
        answers=[]
        index_answer=[]
        
        
        for n in nums:
                    revisedList.append(n)
        
       
        finalI = len(revisedList)
        for i in range(0,finalI):
            initialNumber = revisedList[i]
            remainingT = target - initialNumber
            for j in range(i+1,finalI):
                if remainingT == revisedList[j]:
                    answers.append(initialNumber)
                    answers.append(revisedList[j])
        for answ in answers:
            if answ in nums:
                index_answer.append(nums.index(answ))
                nums[nums.index(answ)] = "x"
        return(index_answer)
        
        
soln = Solution()
print(soln.twoSum([0,4,3,0],0))
# (soln.twoSum([3,2,4],6))
# (soln.twoSum([3,3],6))
