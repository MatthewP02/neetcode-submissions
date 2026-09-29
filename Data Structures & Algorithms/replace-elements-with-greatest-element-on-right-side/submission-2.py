class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        ans = [0] * len(arr)

        for i in range(len(arr)-1, -1, -1):
            ans[i] = greatest
            greatest = max(arr[i], greatest)

        return ans