class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        bool prevZero = true;
        bool justPlaced = false;
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 0) {
                if (prevZero) { // without looking ahead, there seems to be room - place a flower
                    n--;
                    justPlaced = true;
                    prevZero = false;
                } else { // can't place yet, but can in next spot if it's also empty
                    justPlaced = false;
                    prevZero = true;
                }
            } else {
                if (justPlaced) { // placed without looking ahead - cancel it
                    n++;
                    justPlaced = false;
                }
                prevZero = false;
            }
            if (n <= 0 && !justPlaced) {
                return true;
            }
        }
        if (n <= 0) {
            return true;
        } else {
            return false;
        }
    }
};
