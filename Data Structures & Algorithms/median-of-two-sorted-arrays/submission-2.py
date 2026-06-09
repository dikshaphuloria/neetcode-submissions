class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        lenA, lenB = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((lenA+lenB)//2 + 1):
            median2 = median1

            if i < lenA and j < lenB:
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i+=1
                else:
                    median1 = nums2[j]
                    j+=1

            elif i < lenA:
                median1 = nums1[i]
                i+=1

            else:
                median1 = nums2[j]
                j+=1

        
        if (lenA+lenB) % 2 == 1:
            return float(median1)

        else:
            return (median1+median2)/2
