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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> elements;
        for(ListNode* j:lists) {
            while(j) {
                elements.push_back(j->val);
                j=j->next;
            }
        }
        
        sort(elements.begin(),elements.end());
        
        if(elements.size()==0) return NULL;
        
        ListNode* ret=new ListNode(elements[0]);
        ListNode* head=ret;
        for(int i=1;i<elements.size();i++) {
            ret->next=new ListNode(elements[i]);
            ret=ret->next;
        }
        return head;
    }
};
