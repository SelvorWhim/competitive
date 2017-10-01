#include <iostream>
#include <algorithm>
//#include <sstream>
#include <string>
//#include <set>
//#include <vector>
//#include <map>
#include <cmath>

using namespace std;

struct person {
	int max;
	int index;
};

bool maxsort (person i,person j) { return (i.max<j.max || (i.max==j.max && i.index > j.index)); }
//bool indsort (person i,person j) { return (i.index<j.index); }

int main() {
	// units are cents
	int cases;
	cin >> cases;
	int p, n;
	while(cases--){
		cin >> p >> n;
		person peeps[n];
		int ress[n];
		for(int i=0;i<n;i++){
			int max1;
			cin>>max1;
			peeps[i] = person{max1,i};
		}
		
		sort(peeps,peeps+n,maxsort); // ascending, by max prepared to pay
		float fair = (float)p / n;
		int p_left = p;
		//bool possible = true;
		for(int i=0;i<n;i++){
			int m = peeps[i].max;
			if(m < fair){
				ress[peeps[i].index] = m; // if you can't pay fair, pay your maximum
				p_left -= m;
			}
			else{
				m = floor(fair);
				ress[peeps[i].index] = m;
				p_left -= m;
			}
			fair = (float)p_left / (n-i-1);
		}
		if(p_left > 0){
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			for(int i=0;i<n;i++){
				cout << ress[i];
				if(i<n-1){
					cout << " ";
				}
				else{
					cout << endl;
				}
			}
		}
	}
	//int n,m;
	//cin >> n >> m; // read 2
	//cout << "NO" << endl; // print 2. endl is like a linebreak
	return 0;
}
