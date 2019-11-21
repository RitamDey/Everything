#include <boost/date_time/gregorian/gregorian.hpp>
#include <algorithm>
#include <iostream>
using namespace std;


int main() {
    string date;
    vector<boost::gregorian::date> date_vector;

    for (int i=0; i < 10; i++) {
        cout << "Enter a date (yyyy/mm/dd): ";
        cin >> date;

        date_vector.push_back(boost::gregorian::from_string(date));
    }

    sort(date_vector.begin(), date_vector.end());

    for_each(date_vector.begin(), date_vector.end(), [](auto d) { cout << d << endl; });

    return 0;
}
