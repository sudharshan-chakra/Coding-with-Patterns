class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        max_right = arr[-1]

        for i in range(length-2,-1,-1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(temp, max_right)
        
        arr[-1] = -1
        return arr

