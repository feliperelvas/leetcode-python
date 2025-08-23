"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negativo não é palindromo
        if x < 0: return False

        # Contando o numero de algarismos
        num_abs = abs(x)
        contador_tamanho = 0
        while num_abs//10**contador_tamanho != 0:
            contador_tamanho += 1
        if contador_tamanho == 1: return True

        # Testando se é palindromo
        for i in range(contador_tamanho//2):
            num_esq = (num_abs//10**(contador_tamanho//2))//10**(contador_tamanho//2-(i+1))%10 if contador_tamanho%2 == 0 else (num_abs//10**(contador_tamanho//2+1))//10**(contador_tamanho//2-(i+1))%10
            num_dir = (num_abs%10**(contador_tamanho//2))%10**(i+1)//(10**i)
            if num_esq != num_dir:
                return False
        return True