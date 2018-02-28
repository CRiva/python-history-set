# History Set #

A Set implementation that tracks added and removed elements.

## Usage ##

~~~python
>>> from history_set import HistorySet
>>> history_set = HistorySet([1, 2, 3])
>>> history_set.add(4)
>>> history_set                   # Prints: {1, 2, 3, 4}
>>> history_set.added()           # Prints: {4}
>>> history_set.remove(1)
>>> history_set                   # Prints: {2, 3, 4}
>>> history_set.removed()         # Prints: {1}
~~~

## Special case ##

By default, if an element is added and later removed, it will not be tracked in history

~~~python
>>> history_set = HistorySet([1, 2, 3])
>>> history_set.add(4)
>>> history_set.remove(4)
>>> history_set.added()           # Prints: set()
>>> history_set.removed()         # Prints: set()
~~~

If you require these elements to be tracked, you can construct the object with the `eidetic` keyword argument

~~~python
>>> history_set = HistorySet([1, 2, 3], eidetic=True)
>>> history_set.add(4)
>>> history_set.remove(4)
>>> history_set.added()           # Prints: {4}
>>> history_set.removed()         # Prints: {4}
~~~

## Test ##

You can run the tests using [tox](https://tox.readthedocs.io/en/latest/)

~~~shell
tox
~~~

## Publish ##

To publish a new version of this package your Pypi user needt to be added to the project. (Ask Tjaart to give you access)

~~~shell
# Update version number in setup.py

python setup.py sdist
twine upload dist/*
~~~
