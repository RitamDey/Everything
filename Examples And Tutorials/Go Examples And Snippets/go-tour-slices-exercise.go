package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
    res := [][]uint8 {}

    for i := 0; i < dy; i++ {
        t := []uint8 {}
        for j := 0; j < dx; j++ {
            t := append(t, uint8(i ^ j))
        }
        res = append(res, t)
    }
    return res
}

func main() {
    pic.Show(Pic)
}
