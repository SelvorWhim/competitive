// tested on ideone
#include <iostream>
#include <cstring>

#define STRLEN 101

using namespace std;

void outputline(int casenum, int res){
	cout << "Case ";
	cout << casenum;
	cout << ": ";
	cout << res;
	cout << "\n";
}

int main()
{
	char S[STRLEN], T[STRLEN];
	
	int cases;
	cin >> cases; // right?
	cin.getline (S,STRLEN+2); // skip to next line...
	
	for(int casenum=1; casenum<=cases; casenum++) {
		cin.getline (S,STRLEN+2);
		cin.getline (T,STRLEN+2);
		int len = strlen(S);
		int ns_0=0, ns_1=0, ns_q=0;
		int nt_0=0, nt_1=0;
		char cs, ct;
		for (int i=0; i<len; i++) {
			// count chars in both strings at index:
			cs = S[i];
			ct = T[i];
			if(cs=='0')
				ns_0++;
			if(cs=='1')
				ns_1++;
			if(cs=='?')
				ns_q++;
			if(ct=='0')
				nt_0++;
			if(ct=='1')
				nt_1++;
		}
		if(ns_1 > nt_1){
			outputline(casenum, -1);
			continue;
		}
		int n_q1=0, n_01=0, n_q0=0; // number of character changes of each type
		int n_needswap=0; // number of CHARACTERS that need to be swapped - moves will take half
		n_q1 = nt_1 - ns_1;
		if(n_q1 > ns_q) { // trying to turn more '?' than we have
			n_01 = n_q1 - ns_q; // so turn the rest from 0
			n_q1 = ns_q;
		}
		n_q0 = nt_0 - ns_0;
		if (n_q0<0)
			n_q0 = 0;
		
		int n_charswitch = n_q1+n_01+n_q0;
		for (int i=0; i<len; i++) {
			// count chars in both strings at index:
			cs = S[i];
			ct = T[i];
			if((cs=='0'&&ct=='0') || (cs=='1'&&ct=='1')){
				continue;
			}
			if(cs=='1'&&ct=='0'){
				n_needswap++;
			}
			if(cs=='0'&&ct=='1'){
				if(n_01>0){
					n_01--;
				}
				else{
					n_needswap++;
				}
			}
			if(cs=='?'&&ct=='0'){
				if(n_q0>0){
					n_q0--;
				}
				else{
					n_needswap++;
				}
			}
			if(cs=='?'&&ct=='1'){
				if(n_q1>0){
					n_q1--;
				}
				else{
					n_needswap++;
				}
			}
		}
		outputline(casenum, n_charswitch + (n_needswap/2));
	}
	return 0;
}