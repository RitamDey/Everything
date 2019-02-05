#include <bits/stdc++.h>
#include <algorithm>
#include <cmath>
using namespace std;

vector<string> split_string(string);

// Complete the minimumAbsoluteDifference function below.
int minimumAbsoluteDifference(vector<int> arr, int length) {
    // The sort() in the C++ standard library is used to efficiently sort the vector.
    // The arguments passed are iterators to the begin and end of the vector
    sort(arr.begin(), arr.end());
    int min_diff = abs(arr[0] - arr[1]), diff;

    for (int pos=1; pos < length - 1; ++pos) {
        diff = abs(arr[pos] - arr[pos+1]);

        if (diff < min_diff)
            min_diff = diff;
    }

    return min_diff;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int length;
    cin >> length;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(length);

    for (int i = 0; i < length; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = minimumAbsoluteDifference(arr, length);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

