
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp= nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

                print(nums)

#nums =[5,3,8,6,7,2]
nums=[7,15,12,3]
sort(nums)

print(nums)