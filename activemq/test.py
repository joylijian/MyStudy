[object.h]
#ifdef Py_TRACE_REFS
/* Define pointers to support a doubly-linked list of all live heap objects. */
    #define _PyObject_HEAD_EXTRA        \
        struct _object *_ob_next;   \
        struct _object *_ob_prev;
    #define _PyObject_EXTRA_INIT 0, 0, 
#else
    #define _PyObject_HEAD_EXTRA
    #define _PyObject_EXTRA_INIT
#endif

/* PyObject_HEAD defines the initial segment of every PyObject. */
#define PyObject_HEAD           \
    _PyObject_HEAD_EXTRA        \
    int ob_refcnt;          \
    struct _typeobject *ob_type;