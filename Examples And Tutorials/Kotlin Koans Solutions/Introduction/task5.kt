val month = "(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)"

// The `"""` strings are what `r""` strings in Python.
// Also since the triple-quoted strings are raw-strings, string interpolation needs the `${}` syntax
fun getPattern(): String = """\d{2} ${month} \d{4}"""
