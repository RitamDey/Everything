# The `cdef` statment is used to declare a C function that is not
# accessible to the Python Interpreter
cdef int test(int x):
    cdef int y = 0  # declare a Python Integer object in C
    for i in range(x+1):
        y += i
    return y


# The `cpdef` statment is used to declare a Python function that
# is accessible to Python but is implemented in C
cpdef int c_test(int x):
    cpdef y = test(x)  # declare a generic Python Object in C
    return y


# The `def` statment is used to declare a normal python function 
# that is accessible only to Python
def py_test(x):
    y = 0
    for i in range(x+1):
        y += i
    return y

