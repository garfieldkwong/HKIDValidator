import doctest
import importlib
for item in ('.calculator', '.misc', '.validator'):
    doctest.testmod(importlib.import_module(item, __package__))
