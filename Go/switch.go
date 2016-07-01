package main

import "fmt"

func main() {
  fmt.Print("Enter a Number ")
  var n byte
  var d string
  fmt.Scanf("%d",&n)
  switch n {
  case 1:d="1"
  case 2:d="2"
  case 3:d="3"
  case 4:d="4"
  default:d="Unknown Number"
  }
  fmt.Println(d)
}
