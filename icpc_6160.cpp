// can we brute force this?

// numbers are pre-chosen, so we just have 6 numbers (from a known set) and a target
// multiple solutions may be valid, no need to find the shortest one

// number of options: we have 6 numbers which can only be used multiple times if they appear multiple times, so 6 "tiles", each 2 of which can be combined in any of 4 ways
// subtraction and division are not commutative, but because only positive integers can be the result of any operation, that leaves only one valid option for each possible operation (unless it's a number divided by itself, but that's like 1 option)
// each operation reduces the available values by 1, down to at least 1, so there will be at most 5 operations per path, with 4 options in each - 4^5=1024
// can look at it like this: first pick an order for the tiles, then pick the operations and check every partial path, if result is closer than closest previous result, remember the path (only the best so far needs to be remembered like 11 extra spaces in memory). If exact match is found, stop and output, else search exhaustively and output best path found. (Some strict order on these searches needs to be maintained.) Initialize with the closest of the basic values (we have an example where one of the tiles equals the target and there's 0 operations)
// 6!=720 for number ordering, 1024 for operation choice, that's 737k paths to check, 5 mathematical operations per path with some extra boolean checks, should be about 10-15 operations per path on average (extra 11 whenever result is better, that shouldn't happen too often), total is close to 10M PER CASE if search is exhaustive, I don't know how the answers are distributed so I can't tell how long the search will be on average...

// hang on, there's an order of operations thing going on as well...shoot.
// you choose 2 numbers out of 6 and 1 operation out of 4. Then you choose 2 numbers out of the 5 remaining, and an operation out of 4...
// (6 choose 2) * (5 choose 2) * (4 choose 2) * (3 choose 2) * (2 choose 2) = 15*10*6*3=2700, that's almost 4 times as many as I originally estimated, I'll have to hope the distribution is favorable because I don't see much of a general heuristic for reducing the search space...
// division will often not be an option (especially with the large numbers) but the rest of the operations will be allowed one way or another

// plus, hey, the contestants get 30 seconds to solve one measly problem, and my program has to solve up to 50 in 5 seconds?!





#include <iostream>
#include <algorithm>
//#include <sstream>
#include <string>
//#include <set>
#include <vector>
//#include <map>
//#include <stack>
#include <cmath>

using namespace std;

struct oppair {
    int n1;
    char op;
    int n2;
	int res;
};


int nums[6];
int T;
int best_d; // distance of best solution found so far from T (absolute value)
vector<oppair> best_seq;

vector<oppair> opseq; // mostly used as stack but not only
// copy operation sequence - only done when a sequence with a better solution is found
void save_sol(){
	best_seq.clear();
	for(int i=0;i<opseq.size();i++){
		best_seq.push_back(opseq[i]);
	}
}

vector<int> remaining;
// different dfs, uses global stack
// each internal call is inside double/triple loop so complexity may be greater...
// bool says whether exact solution was found
bool dfs()
{
	if(opseq.size()>0 && abs(T-(opseq.back().res)) < best_d){
		best_d = abs(T-(opseq.back().res));
		save_sol();
		if(best_d==0){
			return true;
		}
	}
	
	int n = remaining.size();
    for(int i=0; i<n; i++) // removed auto thing for c++ 11..?
    {
		int n1 = remaining[i];
		for(int j=i+1; j<n; j++){ // changing from j=0 to j=i+1 sped up the code almost twice and pushed it to just fast enough
		// wait actually that's about double at every depth level - even better!
			if(j==i) continue; // for all pairs of indexes i!=j
			int n2 = remaining[j];
			// remove the 2
			if(i>j){ // make sure order is right for indexing
				remaining.erase (remaining.begin()+i);
				remaining.erase (remaining.begin()+j);
			}
			else{ // j > i
				remaining.erase (remaining.begin()+j);
				remaining.erase (remaining.begin()+i);
			}
			// no good way to enumerate operations, so just explicit...
			// op +:
			opseq.push_back(oppair{n1,'+',n2,n1+n2});
			remaining.push_back(n1+n2);
			if(dfs())
				return true;
			remaining.pop_back();
			opseq.pop_back();
			// op *:
			opseq.push_back(oppair{n1,'*',n2,n1*n2});
			remaining.push_back(n1*n2);
			if(dfs())
				return true;
			remaining.pop_back();
			opseq.pop_back();
			// // for the other 2, order numbers so operation (may) result in positive integer
			// if(n1<n2){
				// int temp = n1;
				// n1 = n2;
				// n2 = temp;
			// }
			// // now n1>=n2
			// nope, the following instead to preserve indexes for insert later
			int m1 = max(n1,n2);
			int m2 = min(n1,n2);
			// op -:
			if(m1 != m2){ // assuming no 0 allowed and to prevent division by 0 later
				opseq.push_back(oppair{m1,'-',m2,m1-m2});
				remaining.push_back(m1-m2);
				if(dfs())
					return true;
				remaining.pop_back();
				opseq.pop_back();
			}
			// op /:
			if(m1 % m2 == 0){ // only exact division
				opseq.push_back(oppair{m1,'/',m2,m1/m2});
				remaining.push_back(m1/m2);
				if(dfs())
					return true;
				remaining.pop_back();
				opseq.pop_back();
			}
			// reset values when going back up dfs
			if(i<j){
				remaining.insert(remaining.begin()+i, n1);
				remaining.insert(remaining.begin()+j, n2);
			}
			else{
				remaining.insert(remaining.begin()+j, n2);
				remaining.insert(remaining.begin()+i, n1);
			}
		}
    }
	return false;
}

int main() {
	int cases; // C
	cin >> cases;
	for(int i=0; i<cases; i++){
		best_seq.clear(); // without this I got a hard-t0-find bug where a trivial solution following a nontrivial one printed the old solution instead
		best_d = 1000; // we can do better
		int best_approx; // for trivial solutions
		// read case
		for(int j=0;j<6;j++){
			cin >> nums[j];
		}
		cin >> T;
		// check for trivial solutions
		for(int j=0;j<6;j++){
			if(abs(T-nums[j]) < best_d){
				best_d = abs(T-nums[j]);
				best_approx = nums[j];
			}
		}
		if(best_approx != T){ // no trivial solution, may be a trivial approximation
			remaining = vector<int>(6);
			for(int j=0;j<6;j++){
				remaining[j] = nums[j];
			}
			dfs();
			// clear for next case
			remaining.clear();
			opseq.clear();
		}
		// output best found
		cout << "Target: " << T << endl;
		for(int j=0; j<best_seq.size(); j++){ // if trivial was best approx, will skip
			oppair op = best_seq[j];
			cout << op.n1 << " " << op.op << " " << op.n2 << " = " << op.res << endl;
		}
		cout << "Best approx: ";
		if(best_seq.size()==0){
			cout << best_approx << endl;
		}
		else{
			cout << best_seq.back().res << endl;
		}
		cout << endl;
	}
	return 0;
}
