"""
Example 1:

Input: s = "42"

Output: 42

Explanation:

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
Step 2: "42" (no characters read because there is neither a '-' nor '+')
Step 3: "42" ("42" is read in)

Example 2:

Input: s = " -042"

Output: -42

Explanation:

Step 1: "   -042" (leading whitespace is read and ignored)
Step 2: "   -042" ('-' is read, so the result should be negative)
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)

Example 3:

Input: s = "1337c0d3"

Output: 1337

Explanation:

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)

Example 4:

Input: s = "0-1"

Output: 0

Explanation:

Step 1: "0-1" (no characters read because there is no leading whitespace)
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)

Example 5:

Input: s = "words and 987"

Output: 0

Explanation:

Reading stops at the first non-digit character 'w'.


Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        aux = ''
        contador = 0
        if s == "": return 0
        if len(s) == 1 and not s.isdigit(): return 0
        while True:
            try:
                # Step 1: (leading whitespace is read and ignored)
                while s[contador] == " ":
                    contador += 1
                # Step 2: "   -042" ('-' is read, so the result should be negative)
                if s[contador] == "-" and s[contador+1].isdigit():
                    aux+='-'
                    contador += 1
                elif s[contador] == "+" and s[contador+1].isdigit():
                    aux+='+'
                    contador += 1
                # Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                while s[contador].isdigit():
                    aux+=s[contador]
                    contador += 1
                # Encontrou caracter
                if not s[contador].isdigit():
                    if aux == '':
                        aux='0'
                    break
            except IndexError:
                break
        # Step 4
        try:
            num_final = int(aux)
            if num_final <= -2**31: num_final = -2**31
            elif num_final >= (2**31 - 1): num_final = (2**31 - 1)
            return num_final
        except:
            return 0