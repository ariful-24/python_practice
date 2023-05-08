
def sort(nums):

    for i in range(3):
        minpos=i
        for j in range(i,4):
            if nums[j]<nums[minpos]:
                minpos=j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)





#nums=[5,3,8,6,7,2]
#nums=[3,4,2,5,1]
nums=[7,15,12,3]
sort(nums)
print(nums)