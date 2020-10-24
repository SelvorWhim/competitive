// idea: iterate in reverse, add partial sums, then reverse result

#include <vector>
#include <algorithm>

std::vector<unsigned long long> partsSum(const std::vector<unsigned long long>& ls){
  std::vector<unsigned long long> ret;
  unsigned long long partial_sum = 0;
  ret.push_back(0);
  for (int i = ls.size()-1; i >= 0; i--) {
    partial_sum += ls[i];
    ret.push_back(partial_sum);
  }
  // at this point the return vector has all the partial sums, in reverse order
  std::reverse(ret.begin(), ret.end());
  return ret;
}
