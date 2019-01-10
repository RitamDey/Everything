#include <iostream>
#include <string>
#include <sstream>
#include <exception>
using namespace std;

// To define a custom exception in C++ we need to subclass the class `exception`.
// Here we subclassed the class `exception` then defined a public constructor and defined a public function `what` which is standard exception class method to get a proper message.
class BadLengthException: exception {
    int len;

    public:
        BadLengthException(int len) {
            this->len = len;
        }

        int what() {
            return this->len;
        }
};



bool checkUsername(string username) {
	bool isValid = true;
	int n = username.length();
	if(n < 5) {
		throw BadLengthException(n);
	}
	for(int i = 0; i < n-1; i++) {
		if(username[i] == 'w' && username[i+1] == 'w') {
			isValid = false;
		}
	}
	return isValid;
}

int main() {
	int T; cin >> T;
	while(T--) {
		string username;
		cin >> username;
		try {
			bool isValid = checkUsername(username);
			if(isValid) {
				cout << "Valid" << '\n';
			} else {
				cout << "Invalid" << '\n';
			}
		} catch (BadLengthException e) {
			cout << "Too short: " << e.what() << '\n';
		}
	}
	return 0;
}
