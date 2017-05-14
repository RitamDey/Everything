package main


func swap(x, y int) (int, int) {
    return y, x
}


func ret(x, y int) (string, int, int) {
    return "Values are: ", x, y
}


func main() {
    s, x, y := ret(swap(3, 4))
    println(s, x, y)
}
