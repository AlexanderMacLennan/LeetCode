## Data structure

## 1
if len(set(nums)) != len(nums):
    return True
return False

# More direct
return len(set(nums)) != len(nums)


## 2

nums = [-2,1,-3,4,-1,2,1,-5,4]

# Get position of the highest value : pos_max
max_value = max(nums)
pos_max = nums.index(max(nums))

list_start = nums[0:pos_max]
list_start.reverse()
for

list_end = nums[pos_max:]
list_end.remove(max_value)

# Idea : for each element compare its value with the value of element + next element

#define the element 0
startPoint = maxTotal = nums[0]

for element in nums[1:]:
    startPoint = max(element, startPoint+element)
    maxTotal = max(startPoint, maxTotal)

return maxTotal
