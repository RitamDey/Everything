// Function only submission
// Complete the countApplesAndOranges function below.
void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
  int apple_count = 0;
  int orange_count = 0;
  int tmp;

  for (auto apple: apples) {
    tmp = a + apple;

    if (tmp >= s && tmp <= t)
      apple_count += 1;
  }

  for (auto orange: oranges) {
    tmp = orange + b;

    if (tmp >= s && tmp <= t)
      orange_count += 1;
  }

  cout << apple_count << endl << orange_count << endl;
}
