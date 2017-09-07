
#include <iostream>
#include <algorithm>

#define MAX 100

using namespace std;


int main()
{
    int N,M;
    bool flag = false;
    
    while ( cin >> N >> M) {
        if(flag) {
            cout << endl;
        }
        flag = true;
        
        
        int probs[M+N+1];
    
        for(int i=2; i<M+N+1; i++) {
            probs[i] = 0;
        }
    
        for(int i=1; i <= N;i++) {
            for(int j=1; j <= M; j++){
                probs[i+j]++;
            }
        }
    
        int max=0;

        for(int i=2; i<M+N+1; i++) {
            if(probs[i]>max) {
                //max_id=i;
                max=probs[i];
            }
        }
    
        for(int i=2; i<M+N+1; i++) {
            if(probs[i] == max) {
                cout << i << endl;
            }
        }
        
    
    }
    return 0;
}