/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if (!head || !head->next)
        return head;
    
    struct ListNode *prev = head, *node = head->next;
    head->next = NULL;
    
    while(node) {
        struct ListNode *next = node->next;
        node->next = prev;
        
        prev = node;
        node = next;
    }
    
    return prev;
}

// The one below is ultra-slow:
/*
struct ListNode* reverseListRecursive(struct ListNode* head) {
    if (!head || !head->next)
        return head;

    struct ListNode* reversedList = reverseListRecursive(head->next);

    struct ListNode* end = reversedList;
    while(end->next)
        end = end->next;
    end->next = head;
    head->next = NULL;

    return reversedList;
}
*/
