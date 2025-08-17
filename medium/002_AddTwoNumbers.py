"""
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        inicio = ListNode(0) # placeholder para conseguir utilizar o next, não vai aparecer no final visto que vamos retornar o inicio.next no final
        atual = inicio
        sobra = 0

        while l1 or l2 or sobra:
            valor1 = l1.val if l1 else 0
            valor2 = l2.val if l2 else 0

            soma = valor1 + valor2 + sobra

            sobra = soma // 10 # Resultado da divisao inteira, da o que devemos levar para a próxima casa
            digito = soma % 10 # Resto da divisao por 10, da o digito do nó

            atual.next = ListNode(digito)
            atual = atual.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return inicio.next