package main

import (
	"golang.org/x/tour/wc"
	"strings"
)

func WordCount(s string) map[string]int {
	count := map[string]int{}

	for _, k := range strings.Split(s, " ") {
		// We can use the fact that even if the key was not in map, referencing it would return 0 as runtime makes sure the returned value is the default value of type
		count[k]++
	}

	return count
}

func main() {
	wc.Test(WordCount)
}
