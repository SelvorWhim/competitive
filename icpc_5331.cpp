/*

either keep finding the exchange rate between all pairs of previously seen items, or build a graph and for each query search for a path between the items, multiply along the chain and reduce (with gcd)
	shortest path doesn't matter, there's no contradictory assertions. But also links are unweighted in terms of search so if calculating along a link is a problem, use BFS (will minimize gcd/lcm usages too).
		<=60 items (nodes), at most 1 assertion per pair so < 3600 assertions (edges), BFS should be fine
	partner's template included gcd, see submission for lesson 6

*/


#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <utility> // pair
#include <cmath>

using namespace std;

typedef long long ll;
typedef struct {
	ll num;
	ll den;
} ratio;

set<string> items;
map<string,int> nodenum;
int item_n = 0;
vector<vector<pair<int,ratio>>> g;



ll gcd(ll a, ll b, ll &x, ll &y)
{
    if (a == 0)
    {
        x = 0;
        y = 1;
        return b;
    }
    ll x1, y1;
    ll d = gcd(b%a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return d;
}

inline ll gcd(ll a, ll b) { return gcd(a, b, a, b); }

// reduced multiplied ratio
ratio rmul(ratio r1, ratio r2){
	ll num = r1.num * r2.num;
	ll den = r1.den * r2.den;
	ratio mulled = {num / gcd(num,den), den / gcd(num,den)};
	return mulled;
}

// BFS
// input: an adjacency list describing an undirected/directed graph (g)
// output: the distance of each node from s (dist)
// visible indicates which vertices where already seen
vector<int> visible;
vector<ratio> pathratio;
void bfs(int s, int t)
{
    queue<int> q;
    q.push(s);
    visible[s]=1;
    pathratio[s]={1,1};
    while (!q.empty()) {
        int cur=q.front();
        q.pop();
        for(auto& ver :g[cur])
        {
            if(visible[ver.first]!=0)continue;
            visible[ver.first]=1;
            pathratio[ver.first] = rmul(pathratio[cur], ver.second); // note
			if(ver.first == t){
				break;
			}
            q.push(ver.first);
        }
    }
}


int main() {
	char linetype, chaff;
	string item1, item2;
	int nof1, nof2;
	while(cin >> linetype) {
		if(linetype == '.'){
			break;
		}
		if(linetype == '!'){
			cin >> nof1 >> item1 >> chaff >> nof2 >> item2;
			if(items.find(item1) == items.end()){ // if haven't seen this one before
				items.insert(item1);
				nodenum[item1] = item_n;
				g.push_back(vector<pair<int,ratio>>());
				item_n++;
			}
			if(items.find(item2) == items.end()){ // if haven't seen this one before
				items.insert(item2);
				nodenum[item2] = item_n;
				g.push_back(vector<pair<int,ratio>>());
				item_n++;
			}
			ratio r1 = {nof1, nof2};
			ratio r2 = {nof2, nof1}; // reverse edge
			g[nodenum[item1]].push_back(make_pair(nodenum[item2],r1));
			g[nodenum[item2]].push_back(make_pair(nodenum[item1],r2));
		}
		else{// linetype == '?'
			cin >> item1 >> chaff >> item2;
			// assume both there?
			visible = vector<int>(item_n,0);
			ratio r0 = {0,1};
			pathratio = vector<ratio>(item_n,r0);
			bfs(nodenum[item1], nodenum[item2]);
			if(visible[nodenum[item2]]){
				ratio rres = pathratio[nodenum[item2]];
				cout << rres.num << " " << item1 << " = " << rres.den << " " << item2 << endl;
			}
			else{
				cout << "?" << " " << item1 << " = " << "?" << " " << item2 << endl;
			}
		}
	}
	return 0;
}
