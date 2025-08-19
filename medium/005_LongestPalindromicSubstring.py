"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def ehPalindromo(self, palavra: str) -> bool:
        for i in range(len(palavra)//2):
            if palavra[i] != palavra[len(palavra)-i-1]:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        palindromo_atual = s[0]
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                possivel_palindromo = s[i:j+1]
                if len(possivel_palindromo) <= len(palindromo_atual): continue
                if not self.ehPalindromo(possivel_palindromo): continue
                if len(possivel_palindromo) > len(palindromo_atual):
                    palindromo_atual = possivel_palindromo
        return palindromo_atual

teste_palindromo = Solution()
teste_palindromo.longestPalindrome("jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx")



# teste = "osso"
# teste1 = "arara"
# teste2 = "ana"
# teste3 = "vasco"

# palavra = teste2
# ehPalindromo = True
# for i in range(len(palavra)//2):
#     if palavra[i] != palavra[len(palavra)-i-1]:
#         ehPalindromo = False

# print(ehPalindromo)
saaa = "abcde"
for i in range(len(saaa)-1):
    for j in range(i+1, len(saaa)):
        print(saaa[i:j+1])