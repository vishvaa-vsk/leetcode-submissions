// Last updated: 6/4/2026, 6:38:18 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
         int carry = 0;
        ListNode* final = new ListNode();
        ListNode* currentNode = final;

        while(l1 != nullptr && l2 != nullptr)
        {
            int digit = l1->val + l2->val + carry;
            carry = digit/10;

            currentNode->next = new ListNode(digit%10);
            currentNode = currentNode->next;

            l1 = l1->next;
            l2 = l2->next;
        }

        ListNode *remaining = (l1 == nullptr) ? l2 : l1 ;
        while(l1 != nullptr)
        {
            int digit = l1->val + carry;
            carry = digit/10;
            currentNode->next = new ListNode(digit%10);
            currentNode = currentNode->next;
            l1 = l1->next;
        }
        
        while(l2 != nullptr)
        {
            int digit = l2->val + carry;
            carry = digit/10;
            currentNode->next = new ListNode(digit%10);
            currentNode = currentNode->next;
            l2 = l2->next;
        }

        if(carry > 0)
        {
            currentNode->next = new ListNode(carry);
        }

        return final->next;
    }
};