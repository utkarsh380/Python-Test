list = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]

def findMaxConsecutiveOnes(nums):
        count = 0
        maxcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
                if count >= maxcount:
                    maxcount = count
            else:
                count = 0
        return maxcount 

print(findMaxConsecutiveOnes(list))
