// Last updated: 6/4/2026, 6:37:28 PM
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        // if (k == 1) return head;

        int interval = k;
        bool first_iteration = true;
        ListNode* temp;
        ListNode* reverse = nullptr;
        ListNode* ref = reverse;

        pair<ListNode*, ListNode*> beginnings(head, nullptr); // pointers to the beginnings of intervals so you can link it all together
        ListNode* first = nullptr;

        while (head) {
            temp = head->next;

            head->next = ref;
            ref = head;
            
            if (--interval == 0) {
                if (first_iteration) {
                    first = ref; 
                    beginnings.second = temp;
                    first_iteration = false;
                } else {
                    beginnings.first->next = ref;
                    beginnings.first = beginnings.second;
                    beginnings.second = temp;
                }

                ref = reverse;
                interval = k;
            }

            head = temp;
        }

        while (ref) {
            temp = ref->next;

            ref->next = reverse;
            reverse = ref;

            ref = temp;
        }

        if (first) {
            beginnings.first->next = reverse;
            return first;
        } else {
            return reverse;
        }
    }
};