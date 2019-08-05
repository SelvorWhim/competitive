/* idea: use a min heap of tills (rather than the actual queue),
 * value being the total time spent by that till.
 * for each customer:
 * pop minimum till (the one which will finish soonest)
 * add customer's time to it, and push it back
 * keep track of max till time (so we don't have to pop everything to find it).
 * Using priority_queue as a min heap by using negative values. I'm sure there's a more correct way.
 */
 
 #include <queue>
 
long queueTime(std::vector<int> customers,int n){
  std::priority_queue<int> tills; // negatives for min queue
  int max_till = 0; // max absolute value
  
  for (int i = 0; i < n; i++) {
    tills.push(0); // Q: is there a more compact way to initialize?
  }
  
  for (int customer : customers) {
    int next_till = tills.top();
    tills.pop();
    next_till -= customer; // decrement because negatives
    if (next_till < max_till) { // comparison direction because negatives
      max_till = next_till;
    }
    tills.push(next_till);
  }
  
  return -max_till;
}
