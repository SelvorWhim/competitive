// #include <cassert>
// #include <cctype>
// #include <cmath>
// #include <cstdio>
// #include <cstdlib>
// #include <cstring>
// #include <ctime>
#include <iostream>
// #include <fstream>
// #include <sstream>
// #include <algorithm>
// #include <bitset>
// #include <complex>
// #include <functional>
// #include <limits>
// #include <numeric>
// #include <string>
// #include <tuple>
// #include <utility>
// #include <array>
// #include <vector>
// #include <deque>
// #include <forward_list>
// #include <list>
// #include <stack>
// #include <queue>
// #include <set>
// #include <map>
// #include <unordered_set>
// #include <unordered_map>

using namespace std;

typedef long long ll;

int main(int argc, const char * argv[]) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    srand((unsigned int)time(NULL));
    
    ll s, c, p, l;
    int testcase = 1;
    
    while (cin >> s >> c >> p >> l && (s != 0 || c != 0 || p != 0 || l != 0))
    {
        bool found = false;
        ll x;
        
        for ( x = 0; !found && x <= (int)4e6; ++x)
        {
            if ((l + x) % c == 0 && (p + x) % s == 0)
            {
                
                found = true;
            }
        }
        
        cout << "Case " << testcase << ": ";
        
        if (found)
        {
            --x;
            cout << x / s << ' ' << x%s << '/' << s << endl;
        }
        else
        {
            cout << "Never" << endl;
        }
        
        ++testcase;
    }

    return 0;
}
