"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lista_aux = []
        max_contador = 0
        for i in range(len(s)):
            lista_aux.append(s[i])
            contador = 1
            for j in range(i+1, len(s)):
                if s[j] not in lista_aux:
                    lista_aux.append(s[j])
                    contador += 1
                else:
                    lista_aux = []
                    break
            if contador > max_contador:
                max_contador = contador
        return max_contador