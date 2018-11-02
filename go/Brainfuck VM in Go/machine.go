package main

import (
        "io"
)


type Machine struct {
    code string
    ip   int

    memory [30000] int
    buf    []byte      // A 1 byte buffer to hold the read char
    dp     int

    input   io.Reader  // Object of an implementation of io.Reader
    output  io.Writer  // Object of an implementation of io.Writer
}


func NewMachine(code string, in io.Reader, out io.Writer) *Machine {
    // Return the address of a instance of new Machine type
    return &Machine {
            code:   code,
            input:  in,
            output: out,
            buf:    make([]byte, 1),  // A 1 byte slice as input buffer
    }
}


func (m *Machine) Execute() {
    for m.ip < len(m.code) {
        ins := m.code[m.ip]

        switch ins {
            case '+':
                m.memory[m.dp]++
            case '-':
                m.memory[m.dp]--
            case '>':
                m.dp++
            case '<':
                m.dp--
            case ',':
                m.readChar()
            case '.':
                m.putChar()
            case '[':
                // If the current cell is zero
                // then move to the instruction right after matching ]
                if m.memory[m.dp] == 0 {
                    // Since we are already in a loop, start the depth
                    // with 1, a value of zero indicates a matching ']'
                    depth := 1
                    for depth != 0 {
                        // Increment the instruction pointer as a
                        // matching ] will only be furthur in source
                        m.ip++
                        switch m.code[m.ip] {
                            case '[':
                                depth++
                            case ']':
                                depth--
                        }
                    }
                }
            case ']':
                // If the current cell is non-zero, the find the
                // matching [, and start executing after that
                if m.memory[m.dp] != 0 {
                        depth := 1
                        for depth != 0 {
                            m.ip--
                            switch m.code[m.ip] {
                                case ']':
                                    depth++
                                case '[':
                                    depth--
                            }
                        }
                }
        }

        m.ip++
    }
}


func (m *Machine) readChar() {
        n, err := m.input.Read(m.buf)

        if err != nil {
            panic(err)
        }

        if n != 1 {
            panic("Wrong number of bytes read")
        }
}


func (m *Machine) putChar() {
        m.buf[0] = byte(m.memory[m.dp])

        n, err := m.output.Write(m.buf)

        if err != nil {
                panic(err)
        }

        if n != 1 {
                panic("Wrong number of bytes written")
        }
}
