#define PY_SSIZE_T_CLEAN

#include <Python.h>
#include <stdio.h>


/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject pointer to the Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %zd: %s\n", i,
			       item->ob_type->tp_name);
		}
	}
	else
	{
		printf("[.] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes
 * @p: PyObject pointer to the Python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *data;

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		data = PyBytes_AsString(p);

		printf("  trying string: %s\n", data);
		printf("  first %zd bytes:", (size < 10 ? size : 10));
		for (i = 0; i < size && i < 10; i++)
		{
			printf(" %02x", (unsigned char)data[i]);
		}
		printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints basic info about Python float
 * @p: PyObject pointer to the Python float
 */
void print_python_float(PyObject *p)
{
	double value;

	if (PyFloat_Check(p))
	{
		value = PyFloat_AsDouble(p);
		printf("[.] float object info\n");
		printf("  value: %lf\n", value);
	}
	else
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
	}
}
