#include <Python.h>
#include <numpy/arrayobject.h>
#include "chi2.h"


static char module_docstring[] = "This module provides an iterface for calculating chi-squared using C";
static char chi2_docstring[] = "Calculate the chi-squared of some data given a model.";

static PyObject *chi2_chi2(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
    {"chi2", chi2_chi2, METH_VARARGS, chi2_docstring},
    {NULL, NULL, 0, NULL}
};



PyMODINIT_FUNC init_chi2(void) {
    PyObject *module = Py_InitModule("_chi2", module_methods, module_docstring);
    if(module == NULL)
        return;
    
    /* Load `numpy` functionality */
    import_array();
}


static PyObject *chi2_chi2(PyObject *self, PyObject *args) {
    double m, b;
    PyObject *x_obj, *y_obj, *yerr_obj;

    /**
    * Parse the input table 
    * The PyArg_ParseTuple() function takes two required arguments: 
    * 1. a tuple containg the arguments
    * 2. the format specifier for the argumets
    * 3. The last argumets are the ponters to the C variables. 
    *
    * In this example `d` parses the Python Objects as C doubles
    * And the `O` is used when we want the generic objects to be returned
    * If argument parsing fails then NULL is returned
    **/
    if(!PyArg_ParseTuple(args, "ddOOO", &m, &b, &x_obj, &y_obj, &yerr_obj))
        return NULL;

    /**
     * Intercept the input object as numpy arrays
     * PyArray_FROM_OTF() is used to convert any arbitary Python Object to a Python array object with a specific built-in with a set of requirements
     * NumPy Array C API https://docs.scipy.org/doc/numpy/reference/c-api.array.html
     * Other specific help on PyArray_FROM_OTF() https://docs.scipy.org/doc/numpy/user/c-info.how-to-extend.html#PyArray_FROM_OTF
     * The first argument is the generic object itself.
     * The second argument is the enumeratted flag that will be used to construct array with this type. Here NPY_DOUBLE means all the object in the array will be type of NumPy's double type.
     * The requirements flag allows specification of what kind of array is acceptable. If the object passed in does not satisfy this requirements then a copy is made so that thre returned object will satisfy the requirements. these ndarray can use a very generic pointer to memory. Here NPY_IN_ARRAY is used which is equivalent to NPY_ARRAY_C_CONTIGUOUS | NPY_ARRAY_ALIGNED. This combination of flags is useful for arrays that must be in C-contiguous order and aligned. These kinds of arrays are usually input arrays for some algorithm.
    **/
    PyObject *x_array = PyArray_FROM_OTF(x_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *y_array = PyArray_FROM_OTF(y_obj, NPY_DOUBLE, NPY_IN_ARRAY);
    PyObject *yerr_array = PyArray_FROM_OTF(yerr_obj, NPY_DOUBLE, NPY_IN_ARRAY);

    /* How many data points are there? */
    int N = (int)PyArray_DIM(x_array, 0);

    /* Get pointers to the data as C-types. */
        double *x = (double *)PyArray_DATA(x_array);
        double *y = (double *)PyArray_DATA(y_array);
        double *yerr = (double *)PyArray_DATA(yerr_array);

    /* Call the actual C function to compute the chi-squared. */
    double value = chi2(m, b, x, y, yerr, N);

    /* Clean up objects */
    Py_DECREF(x_array);
    Py_DECREF(y_array);
    Py_DECREF(yerr_array);

    if(value < 0.0) {
        PyErr_SetString(PyExc_RuntimeError, "Chi-squared returned imposible value.");
        return NULL;
    }

    /** 
      * Build the output
      * Create a new value based on a format string similar to those accepted by the PyArg_Parse*() family of functions and a sequence of values. Returns the value or NULL in the case of an error; an exception will be raised if NULL is returned.
      *
      * Py_BuildValue() does not always build a tuple. It builds a tuple only if its format string contains two or more format units. If the format string is empty, it returns None; if it contains exactly one format unit, it returns whatever object is described by that format unit. To force it to return a tuple of size 0 or one, parenthesize the format string.
      *
     **/
    PyObject *ret = Py_BuildValue("d", value);
    return ret;
}

