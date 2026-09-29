class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = 0
        i = len(arr) - 1

        while i >= 0:
            if arr[i] > highest:
                temp = highest
                highest = arr[i]
                arr[i] = temp
            else:
                arr[i] = highest

            i -= 1
        
        arr[-1] = -1
        return arr