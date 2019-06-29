#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
    vector<int> nums;
    for (int i=1; i <= 10; ++i) nums.push_back(i);
    random_shuffle(nums.begin(), nums.end());

    auto isEven = [](int n) { return n%2 == 0; };
    auto display = [](int n) { cout << n << " "; };

    // std::partition() partitions the entire collection into two parts based on the supplied predicate and return a iterator to the point where the end of the true part.
    // This point can also be retrieved using the std::partition_point()

    auto point = partition(nums.begin(), nums.end(), isEven);
    for_each(nums.begin(), point, display);
    cout << endl;

    for_each(point, nums.end(), display);
    cout << endl;

    return 0;
}
