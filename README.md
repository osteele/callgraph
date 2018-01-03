# Callgraph Magic

Callgraph is a Python package that uses GraphViz to draw [dynamic call graphs](https://en.wikipedia.org/wiki/Call_graph)
of Python function calls.

It's intended for classroom use, but may also be useful for self-guided
exploration.

The package defines a Jupyter [IPython](https://ipython.org) [magic](http://ipython.readthedocs.io/en/stable/interactive/magics.html),
`%callgraph`, that displays a call graph within a Jupyter cell:

```python
from functools import lru_cache

@lru_cache()
def lev(a, b):
    if "" in (a, b):
        return len(a) + len(b)

    candidates = []
    if a[0] == b[0]:
        candidates.append(lev(a[1:], b[1:]))
    else:
        candidates.append(lev(a[1:], b[1:]) + 1)
    candidates.append(lev(a, b[1:]) + 1)
    candidates.append(lev(a[1:], b) + 1)
    return min(candidates)

%callgraph -w10 lev("big", "dog"); lev("dig", "dog")
```

![](./docs/images/lev.svg)

It also provides a Python decorator `callgraph.decorator`, that instruments a
function to collect call graph information and render the result:

## Jupyter Usage

```bash
$ pip install callgraph
```

In a Jupyter notebook:

```python
%load_ext callgraph

def nchoosek(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)

%callgraph nchoosek(4, 2)
```

See <https://github.com/osteele/callgraph/blob/master/callgraph-magic-examples.ipynb.ipynb>
for additional instructions and examples.

## Decorator Usage

```bash
$ pip install callgraph
```

```python
from functools import lru_cache
import callgraph.decorator as callgraph

@callgraph()
@lru_cache()
def nchoosek(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)

nchoosek(5, 2)

nchoosek.__callgraph__.view()
```

See <https://github.com/osteele/callgraph/blob/master/callgraph-decorator-examples.ipynb.ipynb>
for additional instructions and examples.

## Development

Install dev tools, and set up a Jupyter kernel for the current python enviromnent:

```bash
$ pip install flit
$ pip install ipykernel
$ python -m ipykernel install --user
```

Install locally:

```bash
flit install --symlink
```

## Acknowledgements

Callgraph uses the Python [graphviz](https://github.com/xflr6/graphviz) package.
Python graphviz uses [Graphviz](https://www.graphviz.org).

## License

MIT
