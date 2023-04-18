#include "/usr/include/python3.4/bytesobject.h"

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t i;

	printf("[*] Python list info");
	printf("[*] Size of the Python List = %ld", var->ob_size);
	printf("[*] Allocated = %ld", list->allocated);

	for (i = 0; i < var->ob_size; i++)
	{
		printf("Element %ld: %s", i, Py_TYPE(list->ob_item[i])->tp_name);
		if (strcmp(Py_TYPE(list->ob_item[i])->tp_name, "bytes") == 0)
		{
			printf("Size of the bytes: %ld", PyBytes_Size(list->ob_item[i]));

			printf("Trying string: %s", PyBytes_AsString(list->ob_item[i]));

			printf("First %ld bytes: ", PyBytes_Size(list->ob_item[i]) < 10 ? PyBytes_Size(list->ob_item[i]) + 1 : 10);
			for (int j = 0; j < PyBytes_Size(list->ob_item[i]) && j < 10; j++)
			{
				printf("%02hhx", ((char *)PyBytes_AsString(list->ob_item[i]))[j]);
				if (j < PyBytes_Size(list->ob_item[i]) - 1 && j < 9)
					printf(" ");
			}
			printf("");
		}
	}
}
