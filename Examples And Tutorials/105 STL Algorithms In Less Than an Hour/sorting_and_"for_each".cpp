#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


bool descending(int i, int j) {
    return i > j;
}


int main() {
    auto display = [](int n) { cout << n << " "; };
    vector<int> nums;
    for (int i=1; i <= 10; ++i)  nums.push_back(i);

    cout << "Sorting via std::sort()" << endl;
    random_shuffle(begin(nums), end(nums));
    // The standard sorting function. Sort the entire collection. Sort by ascending order
    sort(begin(nums), end(nums));
    for_each(nums.begin(), nums.end(), display);
    cout << endl;
    // We can also supply a custom comparision function to change how the sorting is done
    sort(nums.begin(), nums.end(), descending);
    for_each(nums.begin(), nums.end(), display);
    cout << endl;
    cout << "==========================================================================" << endl;

    cout << "Sorting using std::partial_sort()" << endl;
    random_shuffle(begin(nums), end(nums));
    // partial_sort() sorts the [first, middle) part of the collection. The ordering of the remaining collection is not guranteed.
    partial_sort(nums.begin(), nums.begin() + 5, nums.end());
    for_each(nums.begin(), nums.end(), display);
    cout << endl;
    // It also takes a comparator function to change how the sorting is done
    partial_sort(nums.begin(), nums.begin() + 5, nums.end(), descending);
    for_each(nums.begin(), nums.end(), display);
    cout << endl;
    cout << "==========================================================================" << endl;

    cout << "Sorting using std::nth_element()" << endl;
    random_shuffle(begin(nums), end(nums));
    // nth_element() sorts the collection in such a way that the element in the nth will would be the same as the nth element in the sorted collection
    // The ordering of the rest of the collection is not guranteed
    nth_element(nums.begin(), nums.begin() + 5, nums.end());
    for_each(nums.begin(), nums.end(), display);
    cout << endl;

    // It also takes a comparator function to sort the collection in custom ordering
    nth_element(nums.begin(), nums.begin() + 5, nums.end(), descending);
    for_each(nums.begin(), nums.end(), display);
    cout << endl;
    cout << "==========================================================================" << endl;

    cout << "Sorting using std::inplace_merge()" << endl;
    random_shuffle(nums.begin(), nums.end());
    
    sort(nums.begin(), nums.begin() + 5);
    sort(nums.begin() + 5, nums.end());

    // std::inplace_merge() is used to merge when the sorted [first, middle) and [middle, last) to produce a sorted collection. It also takes a comparator
    inplace_merge(nums.begin(), nums.begin() + 5, nums.end());
    for_each(nums.begin(), nums.end(), display);
    cout << endl;

    return 0;
}
