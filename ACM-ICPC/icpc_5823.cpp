/* PLANNING */
// we have probability of getting a point on any given turn, and are asked the probability of winning a game, set and match
// pretty sure there's a closed form formula for solving this, so complexity shouldn't be an issue
// nevermind the score, the point is...points.

//// Game:
// must win at least 4 points and lead by at least 2
// option 1: win first 4 points - p^4
// option 2: win 4 of first 5 points (but not the first 4) - 4(1-p)p^4
// option 3: win 4 of first 6 points (with a win at the end) - (5 choose 2)*(1-p)^2*p^4
// option 4: if neither player won 4 of the first 6 points, it must be 3-3 / 40-40, and now win is determined by lead.
/// The probability of reaching this situation is (6 choose 3)*(1-p)^3*p^3
/// The probability of getting out of a deuce victorious:
//// at a deuce you either win 2 games in a row, or lose 2 games in a row, or win one and lose one among the next 2 games thus getting back to deuce
//// if the probability of winning from a deuce is p1
//// p1=p^2+2p(1-p)p1 -> p1-2p(1-p)p1=p^2->p1=(p^2)/(1-2p(1-p))
// similar for set (if I understood the rules correctly...), simpler for match...




/* CODE */

#include <iostream>
//#include <algorithm>
//#include <sstream>
//#include <string>
//#include <set>
//#include <vector>
//#include <map>
#include <cmath> // pow pow pow!
#include <iomanip> // setprecision

using namespace std;

int main() {
	double p; // probability of winning a point
	while(cin >> p) {
		if(p < 0) {
			break;
		}
		
		// game:
		double pg_tiebreak = pow(p,2)/(1-(2*p*(1-p))); // p1
		double pg = (pow(p,4)) // option 1
			+ (4*(1-p)*pow(p,4)) // option 2
			+ (10*pow((1-p),2)*pow(p,4)) // option 3
			+ (20*pow((1-p),3)*pow(p,3)*pg_tiebreak); // option 4
		
		// set:
		//long double ps_tiebreak = pow(pg,2)/(1-(2*pg*(1-pg))); // like deuce but with pg as base prob // haha NOPE
		/* BAHHH
		my answer for set and match were slightly wrong because the
		tiebreaker was unclearly explained in the instructions...
		I thought they meant keep playing the set till you win by 7 games or more
		had to look up official tennis rules and stuff
		*/
		double ps_tiebreak = pow(p,7) // ok then same logic as pg but goes to 7 points instead of 4...
			+ 7*pow(p,7)*pow(1-p,1)
			+ 28*pow(p,7)*pow(1-p,2)
			+ 84*pow(p,7)*pow(1-p,3)
			+ 210*pow(p,7)*pow(1-p,4)
			+ 462*pow(p,7)*pow(1-p,5)
			+ 924*pow(p,8)*pow(1-p,6)/(2*p*p-2*p+1);
		double ps = (pow(pg,6)) // option 1 - win first 6 games
			+ (6*(1-pg)*(pow(pg,6))) // option 2 - win 6 of 7 games (but not the first)
			+ (21*pow((1-pg),2)*(pow(pg,6))) // option 3 - win 6 of 8 games (but not the first 7) - 7 choose 2
			+ (56*pow((1-pg),3)*(pow(pg,6))) // option 4 - win 6 of 9 games (but not the first 8) - 8 choose 3
			+ (126*pow((1-pg),4)*(pow(pg,6))) // option 5 - win 6 of 10 games (but not the first 9) - 9 choose 4
			//+ (252*pow((1-pg),5)*(pow(pg,6))) // option 6 - win 6 of 11 games (but not the first 10) - 10 choose 5
			+ (252*pow((1-pg),5)*(pow(pg,5))*(pg*pg+2*pg*(1-pg)*ps_tiebreak)); // option 6 - reach 5-5 - 10 choose 5, then win twice or reach 6-6 and play tiebreaker game
		
		// match:
		double pm = ps*ps // win first 2
			+ 2*ps*ps*(1-ps); // win 2 and lose 1, in one of 2 ways (lose the first or the second)
		
		cout << setprecision(11) << fixed // match format of example...
			<< pg << " " << ps << " " << pm << endl; // this prints with the same number of decimal points as them, but still gets presentation error...
	}
	return 0;
}
