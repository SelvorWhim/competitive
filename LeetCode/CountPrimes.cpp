class Solution {
public:
    // ah, it's that problem with the sieve (of Eratosthenes), right? It wouldn't be as efficient to check every number between 1 and n for primality, as long as extra space can be used.
    // basic implementation should take O(n*(log(n))^2) time and O(n) space.
    int countPrimes(int n) {
        if (n < 3) return 0;
        bool composite[n] = {false}; // extra 1 (we're counting LESS than n) so indexes aren't shifted (composite[i] remembers whether i is composite)
        //composite[0] = true;
        //composite[1] = true; // there's a short form for the last 2 but I'm not sure if it's compiler-dependent
        // nvm I'll just ignore these in the loops
        int sn = floor(sqrt(n)); // anything larger won't sieve anything that wasn't sieved already
        for (int i=2; i<=sn; i++) {
            if (!composite[i]) { // if it hasn't been sieved so far, it must be prime, so sieve the rest with it.
                for (int j = 2*i; j < n; j += i) { // sieve all multiples in the array except the prime itself
                    composite[j] = true;
                }
            }
        }
        int primes = 0;
        for (int i=2; i<n; i++) {
            if (!composite[i]) {
                primes++;
            }
        }
        return primes;
    }
};
