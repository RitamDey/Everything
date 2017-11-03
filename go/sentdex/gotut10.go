package main


import ("fmt"
        "net/http"
        "io/ioutil")


func main() {
    // In Go, using a `_` to get a return value discards the value

    // The `http.Get` function is the same as `requests.get` function.
    // It returns a byte-encoded response body and the error code
    resp, _ := http.Get("https://www.washingtonpost.com/news-sitemap-index.xml")

    // The `ReadAll` function is used to read a data from sorce.
    // It returns bytes array and a error statud
    bytes, _ := ioutil.ReadAll(resp.Body)

    // Transform the bytes array into a string
    string_body := string(bytes)

    // Close the response body
    resp.Body.Close()

    fmt.Println(string_body)
}
