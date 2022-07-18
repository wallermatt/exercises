# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def convert_ll_to_str(self):
        num_str = ''
        ll = self
        while ll.next:
            num_str = num_str +  str(ll.val)
            ll = ll.next
        num_str = num_str +  str(ll.val)
        return num_str
    
    def __str__(self):
        return self.convert_ll_to_str()



def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    i1 = convert_ll_to_int(l1)
    i2 = convert_ll_to_int(l2)
    return convert_int_to_ll(i1 + i2)

def convert_ll_to_int(ll):
    num_str = ''
    while ll.next:
        num_str = num_str +  str(ll.val)
        ll = ll.next
    num_str = num_str +  str(ll.val)
    return int(num_str)

def convert_int_to_ll(val):
    num_str = str(val)
    ll = ListNode(int(num_str[0]))
    current_node = ll
    for n in num_str[1:]:
        new_node = ListNode(int(n))
        current_node.next = new_node
        current_node = new_node
    return ll

l1 = ListNode(1)
l2 = ListNode(2)
print(addTwoNumbers(l1, l2))

l1 = convert_int_to_ll(243)
l2 = convert_int_to_ll(564)
print(addTwoNumbers(l1, l2))

l1 = convert_int_to_ll(9999999)
l2 = convert_int_to_ll(9999)
print(addTwoNumbers(l1, l2))
