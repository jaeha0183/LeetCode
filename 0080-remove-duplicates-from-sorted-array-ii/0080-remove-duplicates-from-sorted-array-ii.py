class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # use two pointers
        # i = next valid position
        # j = scans the array
        # since each number can appear at most twice,
        # keep nums[j] only if it differs from nums[i-2]
        
        if len(nums) <= 2:
            return len(nums)

        i = 2

        for j in range(2, len(nums)):
            # if current number is different from previous number:
            if nums[j] != nums[i-2]:
                # put current number at nums[i]
                # move i one step forward
                nums[i] = nums[j]
                i += 1
        return i
            