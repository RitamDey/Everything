#include <Python.h>
#include <malloc.h>


typedef struct LinkedList_LinkedList {
    PyObject_HEAD
    PyObject *data;
    struct LinkedList_LinkedList *next;
    struct LinkedList_LinkedList *prev;
} LinkedList_LinkedList;


static PyTypeObject LinkedList_LinkedListType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "LinkedList.LinkedList",
    sizeof(LinkedList_LinkedList),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT,
    "Linked List",
};


static void LinkedList_dealloc(PyObject *self) {
    self = (LinkedList_LinkedList *)self;
    if(self->next)
        free(self->next);
    if(self->prev)
        free(self->prev);
    
    Py_XDECREF(self->data);
    Py_TYPE(self)->tp_free((PyObject *)self);
}


static PyModuleDef LinkedListmodule = {
    PyModuleDef_HEAD_INIT,
    "LinkedList",
    "Linked List implementation",
    -1,
    NULL, NULL, NULL, NULL, NULL
};


PyMODINIT_FUNC PyInit_LinkedList(void) {
    PyObject *m;
    LinkedList_LinkedListType.tp_new = PyType_GenericNew;
    
    if(PyType_Ready(&LinkedList_LinkedListType) < 0)
        return NULL;
    
    m = PyModule_Create(&LinkedListmodule);
    
    if(m == NULL)
        return NULL;

    Py_XINCREF(&LinkedList_LinkedListType);
    PyModule_AddObject(m, "LinkedList", (PyObject *)&LinkedList_LinkedListType);
    return m;
}

