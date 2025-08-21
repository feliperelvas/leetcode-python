"""
Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
"""

class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        novo_num = 0
        INT_POS = 2**31 - 1
        INT_NEG = -2**31
        if str_num[0] == '-':
            for i in range(len(str_num)-1, 0, -1):
                digito = int(str_num[i])
                # condição para não estourar
                if (novo_num < int(INT_NEG / 10)) or (novo_num == int(INT_NEG / 10) and digito > 8):
                    return 0
                novo_num = novo_num*10 - digito
        else:
            for i in range(len(str_num)-1, -1, -1):
                digito = int(str_num[i])
                # condição para não estourar
                if (novo_num > (INT_POS // 10)) or (novo_num == (INT_POS // 10) and digito > 7):
                    return 0
                novo_num = novo_num*10 + digito
        return novo_num