// idea: the number of candles on every day of the holiday makes an arithmetic sequence, so just use the closed formula for the sum of an arithmetic sequence.

#include <iostream>

using namespace std;

int main() {
	int P, K, N;
	cin >> P;
	while (P--) {
		cin >> K >> N;
		int n_candles = (N + 3) * N / 2; // (1+1 + N+1)*N/2
		cout << K << " " << n_candles << endl;
	}
	return 0;
}
