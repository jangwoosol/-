class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        ans=0
        for i in nums:
            if i==1:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=0
        return ans
        