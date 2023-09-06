class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        req_ind = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                req_ind = i-1
                break
        
        if req_ind==-1:
            self.reverse(nums,0, len(nums)-1)
            return nums

        for i in range(len(nums)-1,req_ind,-1):
            if nums[i]>nums[req_ind]:
                nums[i], nums[req_ind] = nums[req_ind], nums[i]
                # print(nums[len(nums)-1:req_ind:-1])
                # nums = nums[:req_ind+1]+nums[len(nums)-1:req_ind:-1]
                break
        self.reverse(nums, req_ind+1, len(nums)-1)

        return  nums
    
    def reverse(self, nums,start, end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

        return nums