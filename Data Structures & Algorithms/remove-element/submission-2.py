class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        """
        1) nums = [2, 5, 2], val = 2 -> 1, nums = [5, 2, 2]
        2) Sort the array and substitute every copy of val with a number that's after 
        it; scan the array and save the indexes into a stack and substitute when you
        find a different number; use two pointers
        """        

        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

        """
        3) nums = [] -> 0; 
        nums = [1], val = 1 -> l = 0, r = 1 -> 0
        nums = [1], val = 0 -> l = 1 -> 1
        nums = [2, 5, 2, 3, 2], val = 2 -> l = 0, r = 1 -> nums = [5, 2, 2, 3, 2]
        -> l = 1, r = 3 -> nums = [5, 3, 2, 2, 2] -> l = 2, r = 5
        nums = [2, 2, 2], val = 2 -> l = 0, r = 3 -> 0
        nums = [5, 5, 5], val = 2 -> l = 3, r = 3 -> 3
        nums = [2, 4, 3, 5], val = 2 -> l = 0, r = 1 -> nums = [4, 2, 3, 5] 
        -> l = 1, r = 2 -> nums = [4, 3, 2, 5]
        4) Time complexity O(n), n = len(nums); space complexity O(1)
        """   