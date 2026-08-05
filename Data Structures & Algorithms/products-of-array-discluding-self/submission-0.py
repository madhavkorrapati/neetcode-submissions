class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            pro=1
            for j in range(len(nums)):
                if i!=j:
                    pro*=nums[j]
            l1+=[pro]
        return l1




