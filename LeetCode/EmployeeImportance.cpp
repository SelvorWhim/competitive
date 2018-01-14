// EDIT: this failed because the assumption below was incorrect. It worked on example cases where it is correct.
// assuming employees are ordered by their ids in the vector, with the employee at index i having id i+1, as in example
// idea: we have a tree structure with access to children and info through indexed structure, do a tree search.

/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        if (id < 1 || id > employees.size()) return 0;
        int sumImportance = employees[id-1]->importance; // personal importance
        for (int& sub_id: employees[id-1]->subordinates) { // sum of importance for subordinate subtree. For "leaf", vector is empty and loop will exit.
            sumImportance += getImportance(employees, sub_id);
        }
        return sumImportance;
    }
};
