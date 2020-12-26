class ParkingSystem {
private:
    int spaces[3]; // 1st value is number of big spaces remaining, 2nd is medium, 3rd is small
public:
    ParkingSystem(int big, int medium, int small) {
        this->spaces[0] = big;
        this->spaces[1] = medium;
        this->spaces[2] = small;
    }
    
    bool addCar(int carType) {
        if (this->spaces[carType-1] > 0) {
            this->spaces[carType-1]--;
            return true;
        }
        else {
            return false;
        }
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
 