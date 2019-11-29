public boolean evenlySpaced(int a, int b, int c) {
    int[] arr = {a, b, c};
    Arrays.sort(arr);

    return (arr[1] - arr[0]) == (arr[2] - arr[1]);
}
