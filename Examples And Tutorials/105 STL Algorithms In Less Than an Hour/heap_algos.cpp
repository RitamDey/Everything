#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    // In C++, the heap implementation is max heap.
    int nums[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    vector<int> numbers(begin(nums), end(nums));

    // Creates the heap
    make_heap(numbers.begin(), numbers.end());
    cout << "Initial heap: " << numbers.front() << endl;

    // Inserting into the heap
    // To insert into the heap, first we directly .push_back() the element into the vector
    // Then use the push_heap() function to create the finalized heap
    numbers.push_back(10);
    push_heap(numbers.begin(), numbers.end());
    cout << "New Heap element: " << numbers.at(0) << endl;
    
    // Removing from the heap
    // The pop_heap() doesn't actually returns the element. It just makes the popped elemeent the last one in the vector.
    // We need to actually remove the element using .pop_back()
    pop_heap(numbers.begin(), numbers.end());
    cout << "Popped element: " << numbers.at(numbers.size() - 1) << endl;
    numbers.pop_back();

    // Using heaps to sort
    // The sort_heap() function uses heaps to sort the underlying vector.
    // Using it transforms the heap into a sorted vector
    for (int i=0; i < numbers.size(); ++i)
        cout << numbers.at(i) << " ";
    cout << endl;

    return 0;
}
