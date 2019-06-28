/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    void reverseK(ListNode* prev, ListNode* node, const int k) {
        if (k > 1) {
            reverseK(node, node->next, k - 1);
        }
        node->next = prev;
    }

public:
    ListNode* reverseKGroup(ListNode* head, const int k) {
        if (k == 1 || head == nullptr)
            return head;
        
        // get k-th node
        ListNode *kthNode = head;
        for(int i = 1; i < k; i++) {
            if(kthNode->next == nullptr) {
                return head;
            }
            kthNode = kthNode->next;
        }
        ListNode *after = kthNode->next;
        
        after = reverseKGroup(after, k);
        
        // reverse k nodes
        reverseK(after, head, k);
        
        return kthNode;
    }
};
