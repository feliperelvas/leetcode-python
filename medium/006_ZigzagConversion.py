"""
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        palavra_final = ''
        for i in range(numRows):
            proximo_indice = i
            indice_aux = 0
            atualizador = (2*(numRows-1)-(i*2),i*2)
            while proximo_indice <= (len(s)-1):
                if atualizador[indice_aux%2] != 0:
                    palavra_final += s[proximo_indice]
                proximo_indice += atualizador[indice_aux%2]
                indice_aux += 1
        return palavra_final