class Solution {
public:
    // equal to the min (number of even factors, number of factors that are multiples of 5). There will always be more factors that are multiples of 2 in a factorial, since consecutive integers where 2 appears first are included, so counting the 5's is enough. For this, integer division by 5.
    // ...but also factors that contain multiple powers of 5 count multiple times (2's still appear much more so it's enough to count the 5's)
    int trailingZeroes(int n) {
        int highestPowOf5 = floor(log(n)/log(5)); // log_5(n)
        int sum = 0;
        int powOf5 = 5;
        for (int i=1; i<=highestPowOf5; i++) {
            sum += n / powOf5;
            powOf5 *= 5;    
        }
        return sum;
    }
};
