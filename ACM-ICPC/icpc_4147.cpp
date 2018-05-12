// v1 - passes simple example and uDebug user supplied example. Sending it up for checking.
// ACCEPTED - run time 0.003s
// time complexity O(T*(2^N)) (keep in mind 2^N is just the number of tournament participants, it's not gonna be huge)

/*  
	///////// SKETCH ///////////
	Dunno how "normal knockout tournaments" work in terms of who is matched against who, gonna assume by pattern that in each level you take the winner of the first pair and match them with the winner of the second for the next level, and the winner of the third with the 4th, etc.
	Player numbers in the first round go from 1 to 2^N, in the next 1 to 2^(N-1). If indexing 0 to 2^N-1, we get either of a pair's next index simply by integer division by 2, so I'll go with that. Need to make sure indexes are shifted on input/output.
	N is small enough to allocate 2^N space easy. Or even allocate 2^10 at the start of the program and use it up to the right place without clearing - why the hell not.
*/

#include <iostream>

using namespace std;

bool present[1024]; // max size

int main() {
	int T,N,M;
	cin >> T;
	while(T--) {
		// read input:
		cin >> N >> M;
		int total = 1 << N;
		for(int i=0; i<total; i++){
			present[i] = true; // there's probably a clear for this...eh
		}
		int absentee;
		for(int i=0; i<M; i++){
			cin >> absentee;
			present[absentee-1] = false; // shift
		}
		
		// bubble up and count:
		int wos = 0; // tales of wo // walkover running count
		for(int level=N; level>0; level--){ // per tournament level
			int level_tot = 1 << level; // TODO: check the numbers
			/*
			// DBG
			cout << "level" << level << endl;
			for(int i=0; i<level_tot; i++){
				cout << present[i] << endl;
			}
			// DBG end
			*/
			for(int i=0; i<level_tot; i+=2){ // note 2 - checking by pairs
				int next_level_i = i/2;
				if(present[i] && present[i+1]){ // both present
					present[next_level_i] = true;
				} else if((!present[i]) && (!present[i+1])){ // both absent
					present[next_level_i] = false;
				} else { // one present
					present[next_level_i] = true;
					wos++;
				}
			}
		}
		
		// present final count!
		cout << wos << endl;
	}
	return 0;
}
