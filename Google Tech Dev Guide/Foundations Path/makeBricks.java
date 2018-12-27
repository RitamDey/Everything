public boolean makeBricks(int small, int ig, int goal) {
    int bigRequired = goal / 5;
    int smallRequired;

    if (bigRequired > big)
        smallRequired = goal - (big * 5);
    else
        smallRequired = goal - (bigRequired * 5);

    return smallRequired <= small;
}
