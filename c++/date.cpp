#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
using namespace std;

class Date {
    public:
    string yy, mm, dd;

    Date(string dd, string mm, string yy) {
        this->dd = dd;
        this->mm = mm;
        this->yy = yy;
    }
    Date() {
    }
    static Date parse(string date) {
        string dd, mm, yy;
        regex d("\\d{2}/\\d{2}/\\d{4}");

        if (regex_match(date, d) == false)
            return Date("-1", "-1", "-1");

        dd = date.substr(0, 2);
        mm = date.substr(3, 2);
        yy = date.substr(6, 4);

        return Date(dd, mm, yy);
    }

    void display() {
        cout << "Day: " << this->dd;
        cout << " Month: " << this->mm;
        cout << " Year: " << this->yy << endl;
    }
    
    bool is_valid() {
        return this->dd != "-1" && this->mm != "-1" && this->dd != "-1";
    }
};


bool date_compare(Date d1, Date d2) {
    // Compare the dates
}


int main() {
    string fname = "dates.txt";
    vector<Date> dates;
    string date;
    Date d;
    ifstream input(fname, ifstream::in);
    int number;

    input >> number;

    cout << "Number of dates: " << number << endl;

    for (int i=1; i <= number; i++) {
        input >> date;

        d = Date::parse(date);

        if (d.is_valid())
            dates.push_back(d);
        else
            cout << "Invalid: " << date << endl;
    }

    sort(dates.begin(), dates.end(), date_compare);

    for (auto d: dates) {
        d.display();
    }

    return 0;
}
