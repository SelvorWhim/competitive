/* this seems trivial, am I missing the point? */

#include <iostream>

using namespace std;

int main() {
	int n;
	double X,Y;
	cin >> n;
	while(n--){
		cin>>X>>Y;
		if(X>=Y){
			cout << "MMM BRAINS" << endl;
		} else {
			cout << "NO BRAINS" << endl;
		}
	}
	return 0;
}
