import callgraph
from functools import lru_cache


@callgraph.decorator(graph_attrs={'size': '8,'})
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


lev("big", "dog")
lev("dig", "dog")

lev.__callgraph__.view()
