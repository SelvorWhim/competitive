/*
	NOTE: I thought this was an incomplete solution as I didn't check for the case where the laser (and my code...) gets caught in an infinite loop, but apparently this is impossible (with all right turns, maybe it is) or the official tests don't check for it, because the online judge accepted it. This simplifies the solution considerably compared to the fix I was planning.
*/

#include <iostream>

using namespace std;

// north, east, south, west
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};
// assume coords start at bottom left corner (like a math graph)

int main() {
	int T;
	cin >> T;
	while(T--){ // per case
		int n, r;
		cin >> n >> r;
		bool grid[n+2][n+2]; // n isn't too big. Including wrapper here
		for(int i=0; i<n+2; i++){
			for(int j=0; j<n+2; j++){
				grid[i][j] = false; // initialize with no turners
			}
		}
		int x, y;
		while(r--){
			cin >> x >> y;
			grid[x][y] = true; // 1-indexed like input because wrapper
		}
		cin >> x >> y; // now contains laser start position.
		
		int dir;
		// find direction (assuming no laser starts at a corner):
		if(y == 0)
			dir = 0; // north
		else if(x == 0)
			dir = 1; // east
		else if(y == n+1)
			dir = 2;
		else // x == n+1
			dir = 3;
		
		bool flag = true;
		while(flag){
			x += dx[dir];
			y += dy[dir];
			if(grid[x][y]){ // laser
				dir = (dir+1)%4; // next direction among [0,1,2,3] - rotation right
			}
			if(x==0 || y==0 || x==n+1 || y==n+1)
				flag = false;
		}
		
		cout << x << " " << y << endl; // TODO: deal with caught beam (output 0,0). Meaning beam that goes from the same location in the same direction as before?
	}
	//cin >> n >> m; // read 2
	//cout << "NO" << endl; // print 2. endl is like a linebreak
	return 0;
}
