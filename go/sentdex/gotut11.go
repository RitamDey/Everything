package main


import ("fmt"
        "net/http"
        "io/ioutil"
        "encoding/xml"  // Required for unpacking the XML bytes
    )

/**
 * Washington Post's sitemap
 * <sitemapindex>
 *  <sitemap>
 *      <loc>...</loc>
 *  </sitemap>
 *  <sitemap>
 *      <loc>...</loc>
 *  </sitemap>
 *  <sitemap>
 *      <loc>...</loc>
 *  </sitemap>
 * </sitemapindex>
**/


type SiteMapIndex struct {
    Locations []Location `xml:"sitemap"`
}


type Location struct {
    Loc string `xml:"loc"` 
}


func (l Location) String() string {
    return fmt.Sprintf(l.Loc)
}


func main() {
    resp, _ := http.Get("https://www.washingtonpost.com/news-sitemap-index.xml")
    bytes, _ := ioutil.ReadAll(resp.Body)
    resp.Body.Close()

    var s SiteMapIndex
    xml.Unmarshal(bytes, &s)  // Unpack the data and put it into s

    fmt.Println(s.Locations)
}
