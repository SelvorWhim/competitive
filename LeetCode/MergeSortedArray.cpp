class Solution {
public:
    // merge into nums1, which according to assumptions has capacity at least n+m
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i_1 = m-1;
        int i_2 = n-1;
        int i = n+m-1;
        for (; i_1 >= 0 && i_2 >= 0; i--) {
            if (nums1[i_1] > nums2[i_2]) {
                nums1[i] = nums1[i_1];
                i_1--;
            } else {
                nums1[i] = nums2[i_2];
                i_2--;
            }
        }
        for (; i_1 >= 0; i_1--, i--) {
            nums1[i] = nums1[i_1];
        }
        for (; i_2 >= 0; i_2--, i--) {
            nums1[i] = nums2[i_2];
        }
    }
};
