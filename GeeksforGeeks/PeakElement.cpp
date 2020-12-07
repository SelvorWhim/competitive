/* The function should return the index of any
   peak element present in the array */
// arr: input array
// n: size of array
int peakElement(int arr[], int n)
{
   if (n==0) throw "nope";
   if (n==1) return 0;
   if (arr[0] >= arr[1]) return 0;
   for (int i = 1; i < n-1; i++) {
       if (arr[i] > arr[i+1]) { // 1 check is enough, the previous is implied by the last iteration
           return i;
       }
   }
   return n-1;
}
