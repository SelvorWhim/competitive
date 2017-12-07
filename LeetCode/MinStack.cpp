// implementation idea: if push and pop happen on a stack, any new minimums added or "revealed" will be in the same order, so there's no need to keep them in any kind of ordered structure, we can keep a separate stack just for the potential minimums. This also makes it possible to do all operations in O(1)
// implementation can be generalized to MinStack of any comparable type
class MinStack {
private:
    stack<int> allStack;
    stack<int> minStack; // contains only decreasing elements of minStack, with minimum at the top. Duplicates for multiple smallest elements with no smaller ones in between. Between operations, this is empty iff allStack is empty.
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int x) {
        allStack.push(x);
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }
    
	// same behavior when stack is empty as regular int stack
    void pop() {
        if (minStack.top() == allStack.top()) {
            minStack.pop();
        }
        allStack.pop();
    }
    
	// same behavior when stack is empty as regular int stack
    int top() {
        return allStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */