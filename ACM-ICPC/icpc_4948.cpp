/*
SKETCH:
start from last year's top team, count how many pairs they appear with - that's how many places down they've gone.
in fact, for every team, the number of teams that were previously above them with whom they've switched is how many places up they've gone, and the number of teams below who switched is how many down they went. Subtract the latter from the first and add to original rank.
E.g. 1 2 3 -> 3 2 1: pairs are (1 2),(2 3),(1 3), 2 has one switch in each direction ending up where it started
Impossible is when two teams end up with the same rank after this calculation.
How would a team end up with undetermined ranking? If there are not enough pairs?
Need a mapping of team to its former rank, and a reverse mapping.
*/

#include <iostream>

using namespace std;

int main() {
	int cases;
	cin >> cases;
	while(cases--){
		// parse old rank:
		int n,t;
		cin >> n;
		int r[n]; // rank of team (0-indexed, note input/output are 1-indexed), last season
		int nr[n]; // new rank of team (0-indexed)
		for(int i=0; i<n; i++){ // per team in the line of old rankings
			cin >> t;
			r[t-1] = i;
			nr[t-1] = i; // initialize new rank as old rank
		}
		
		// parse pairs and calculate new rank:
		int m,t1,t2;
		cin >> m;
		for(int i=0; i<m; i++){ // per pair
			cin >> t1 >> t2;
			if(r[t1-1] > r[t2-1]){
				nr[t1-1]--;
				nr[t2-1]++;
			} else {
				nr[t1-1]++;
				nr[t2-1]--;
			}
		}
		
		// check for duplicates:
		int team[n]; // (0-indexed) team at new rank, should not be entered twice. I'd use set but I know how many there should be so meh.
		bool dup = false;
		for(int i=0; i<n; i++) {
			team[i] = -1;
		}
		for(int i=0; i<n; i++) {
			if(team[nr[i]] == -1) { // no mapping for this rank yet
				team[nr[i]] = i; // reverse mapping
			} else { // already mapped this rank
				dup = true;
				break;
			}
		}
		if(dup) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			for(int i=0; i<n; i++) {
				if(i > 0){
					cout << " "; // moved here to prevent space at end of line (caused presentation error)
				}
				if(team[i] == -1){
					cout << "?"; // indeterminate team at rank
				} else {
					cout << (team[i] + 1); // known team at rank
				}
			}
			cout << endl;
		}
	}
	return 0;
}
