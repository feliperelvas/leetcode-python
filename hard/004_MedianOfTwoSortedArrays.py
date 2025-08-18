"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List

class Solution:
    def calculaMediana(self, lista: List[int]):
        tamanho_lista = len(lista)
        if tamanho_lista % 2 == 0:
            num1 = int(tamanho_lista/2) - 1
            num2 = int(tamanho_lista/2)
            return (lista[num1] + lista[num2])/2
        else:
            return lista[(tamanho_lista//2)]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        lista_aux = []
        for _ in range(m+n):
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    lista_aux.append(nums1[i])
                    i += 1
                else:
                    lista_aux.append(nums2[j])
                    j += 1
            elif i >= m:
                lista_aux.append(nums2[j])
                j += 1
            elif j >= n:
                lista_aux.append(nums1[i])
                i += 1
        return self.calculaMediana(lista_aux)



if __name__ == '__main__':
    teste1 = Solution()
    print(teste1.findMedianSortedArrays([1,4,5],[2,3]))