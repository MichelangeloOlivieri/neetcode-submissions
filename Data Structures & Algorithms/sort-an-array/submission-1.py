class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(left: int, right: int) -> None:
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            merge(left, mid, right)

        def merge(left: int, mid: int, right: int) -> None:
            temp = []

            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= mid:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left + k] = temp[k]
                
        merge_sort(0, len(nums)- 1)
        return nums
        
        """
        Time complexity O(n * log(n)), where n = len(nums); space complexity O(n)
        """