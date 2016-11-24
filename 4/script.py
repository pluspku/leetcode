class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tot = len(nums1) + len(nums2)
        if tot % 2 == 1:
            return self.findKth(nums1, 0, nums2, 0, tot / 2 + 1)
        else:
            return (self.findKth(nums1, 0, nums2, 0, tot / 2) + \
                    self.findKth(nums1, 0, nums2, 0, tot / 2 + 1)) / 2.0

    def findKth(self, A, i, B, j, k):
        oo = float('inf')
        if len(A) <= i:
            return B[j + k - 1]
        if len(B) <= j:
            return A[i + k - 1]

        if (k == 1):
            return min(A[i], B[j])

        x = A[i + k / 2 - 1] if i + k / 2 - 1 < len(A) else oo
        y = B[j + k / 2 - 1] if j + k / 2 - 1 < len(B) else oo
        if x < y:
            return self.findKth(A, i + k / 2, B, j, k - k / 2)
        else:
            return self.findKth(A, i, B, j + k / 2, k - k / 2)

        
        
