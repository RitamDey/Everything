#include <iostream>
#include <vector>
#include <sstream>
using namespace std;


vector<int> parseInt(string str) {
    /**
     * stringstream class is used to convert a simple C++ string into a stream which can be used for reading or writing using regular stream manipulation operators
     **/
    vector<int> integers;
    stringstream stream(str);  // Construct the string stream from a C++ string
    int num;
    char ch;

    // Reading from streams in C++ returns a empty string if the read input doesn't match the type of variable
    while (stream >> num) {
	integers.push_back(num);
	stream >> ch;  // This is used to get rid of the "," from the stream, since leaving them can return empty strings when read to `num`
    }

    return integers;
}


int main() {
    string str;
    cin >> str;

    vector<int> integers = parseInt(str);
    for(int i=0; i < integers.size(); ++i)
	cout << integers[i] << endl;

    return 0;
}
