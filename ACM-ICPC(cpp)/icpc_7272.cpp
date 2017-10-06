// problem 1/2 - which employees always appear in the first A/B of a topological sort?
// problem 3 - which employees always appear after the first B in a topological sort?
// Can I check all options in the topological?
//// no way, that could be like E! I could maybe count them in less but this requires seeing which employees are where in the orderings...
// ok so an employee is certainly not promoted if they have too many people above them (traisitively) (B).
//// If there are fewer, because transitivity those people have fewer above them and can all be promoted and then the employee can be promoted, so that's a sufficient
// similarly certainly promoted if everybody else is below, or enough people below that the rest are less than A/B. So at least E-A/B people below
//// and if there are fewer below, that means there's at least A/B above or "to the side" and they can be promoted before you since you're not above them, so you're not guaranteed

// need to search in reverse for problem 3 so gotta be adjacency matrix

// based on accepted and unaccepted answer, looks like multiple inputs are a thing and outputs should just follow one another with no extra lines


#include <iostream>
#include <algorithm>
//#include <sstream>
#include <string>
#include <set>
#include <vector>
//#include <map>
//#include <cmath>

using namespace std;

#define MAX_N 5001

vector<vector<int> > adj; // adjacency list
vector<vector<int> > rev_adj; // reverse graph adjacency list

set<int> succ; // successors
// DFS
// input: an adjacency list describing an undirected/directed graph (g)
// visible indicates which vertices where already seen
// modified to work on either adj, save set instead of printing, for easy counting
void dfs(vector<vector<int> >& adjl, int s)
{
    //cout<<s<<endl;
	succ.insert(s);
	int n = adjl[s].size();
    for(int i=0; i<n; i++) // removed auto thing for c++ 11..?
    {
		int x = adjl[s][i];
		if(succ.find(x) != succ.end())
			continue;
        dfs(adjl, x);
    }
}

int main() {
	// read - based on 4287
	int A, B, E, P;
	while(cin >> A >> B >> E >> P)
	{
		adj = vector<vector<int> >(E, vector<int>());
		rev_adj = vector<vector<int> >(E, vector<int>());
		for (int i = 0; i < P; i++){
			int s1, s2;
			cin >> s1 >> s2;
			adj[s1].push_back(s2);
			rev_adj[s2].push_back(s1);
		}
		int certain_A = 0; // certain if A are promoted
		int certain_B = 0; // certain if B are promoted
		int nochance_B = 0; // haha nope! How many definitely won't be promoted.
		for (int s = 0; s < E; s++){
			succ.clear();
			dfs(adj, s);
			if(succ.size() > E-B){ // succ.size()-1 = all but the node itself
				certain_B++;
				if(succ.size() > E-A){
					certain_A++;
				}
			}
			succ.clear();
			dfs(rev_adj, s);
			if(succ.size() > B){
				nochance_B++; // boo hoo
			}
		}
		cout << certain_A << "\n" << certain_B << "\n" << nochance_B << "\n";
	}
	return 0;
}
