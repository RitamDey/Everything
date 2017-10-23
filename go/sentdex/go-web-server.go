package main


import (
        "fmt"
        "net/http"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Whoa, Go is neat! <br> <a href='/about'>About</a>")
}


func about_handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Useless Go Server!!")
}
func main() {
    http.HandleFunc("/", index_handler)
    http.HandleFunc("/about", about_handler)
    http.ListenAndServe(":8000", nil)
}
