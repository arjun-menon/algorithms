# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class WrappedNode(ListNode):
    def __init__(self, node):
        ListNode.__init__(self, node.val)
        self.next = node.next
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodeHeap = [WrappedNode(node) for node in lists if node != None]
        if len(nodeHeap) <= 1:
            return [] if not nodeHeap else nodeHeap[0]
        heapq.heapify(nodeHeap)

        rootNode = lastNode = ListNode(0)
        while nodeHeap:
            node = heapq.heappop(nodeHeap)
            if node.next:
                heapq.heappush(nodeHeap, WrappedNode(node.next))
            
            lastNode.next = node
            lastNode = node

        lastNode.next = None        
        return rootNode.next
