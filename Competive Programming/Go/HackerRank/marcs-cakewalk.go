package main

import (
    "fmt"
    "sort"
    "math"
)

func marcsCakewalk(calories []int, len int) int {
    // The comparator function takes indexes not actual values
    sort.Slice(calories, func(i, j int) bool { return calories[i] > calories[j] })
    var sum int = 0

    for k, v := range calories {
        sum += (int(math.Pow(2.0, float64(k))) * v)
    }

    return sum;
}

func main() {
    var n int
    fmt.Scanf("%d", &n);

    calories := make([]int, n)
    for i := 0; i < n; i++ {
        fmt.Scanf("%d", &calories[i])
    }

    fmt.Println(marcsCakewalk(calories, n))
}
