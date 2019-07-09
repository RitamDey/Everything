package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func decode(c byte) byte {
    if c >= 'a' && c <= 'z' {
        return (((c - 'a') + 13) % 26) + 'a'
    } else if c >= 'A' && c <= 'Z' {
        return (((c - 'A') + 13) % 26) + 'A'
    } else {
        return c
    }
}

func (cipher rot13Reader) Read(buf []byte) (int, error) {
        t := make([]byte, 1)
        pos := 0

	for {
		_, err := cipher.r.Read(t)
                if err == io.EOF {
                    break
                }
                buf[pos] = decode(t[0])
                pos++
	}
        return pos, io.EOF
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}

