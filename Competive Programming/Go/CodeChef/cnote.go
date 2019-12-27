package main

import "fmt"


func main() {
    var cases int;
    var poetry_length, pages_left, num_notebooks, budget, pages_req, curr_cost, curr_page uint64;

    fmt.Scanf("%d", &cases);

    for k := 1; k <= cases; k++ {
        fmt.Scanf("%d %d %d %d", &poetry_length, &pages_left, &budget, &num_notebooks)

        pages_req = poetry_length - pages_left;
        notebooks := map[uint64]uint64 {}

        for i := uint64(1); i <= num_notebooks; i++ {
            fmt.Scanf("%d %d", &curr_page, &curr_cost)

            if curr_cost <= budget {
                notebooks[curr_page] = curr_cost;
            }
        }

        flag := false

        for k, _ := range notebooks {
            if k >= pages_req {
                flag = true
                break
            }
        }

        if flag {
            fmt.Println("LuckyChef")
        } else {
            fmt.Println("UnluckyChef")
        }
    }
}
