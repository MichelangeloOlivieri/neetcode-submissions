class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = mountain_arr.length()
        l = 0
        r = n - 1

        while l < r:
            mid = l + (r - l) // 2
            
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
                
        peak = l
        l = 0
        r = peak

        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l = peak + 1
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1
                
        return -1

        """
        - Time complexity O(log(N)), where N = mountainArr.length()
        - Space complexity O(1)
        """