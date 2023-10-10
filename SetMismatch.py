def findErrorNums(nums):
    nums.sort()
    n = len(nums)
    m_set=[]
    i=1
    for i in range(1,n): #To find duplicate element
        if nums[i-1] != nums[i]:
            continue
        else:
            m_set.append(nums[i])
    for i in range(1,n):#For finding missing number
        if (nums[i]-nums[i-1])>1:
            m_set.append(nums[i-1]+1)
        
    
    return m_set    

nums = [5,6,7,7,9]
print(findErrorNums(nums))