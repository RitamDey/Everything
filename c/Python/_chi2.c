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



