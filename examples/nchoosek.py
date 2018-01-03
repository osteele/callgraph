from functools import lru_cache
import callgraph.decorator as callgraph


@callgraph
@lru_cache()
def nchoosek(n, k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)


nchoosek(3, 2)

nchoosek.__callgraph__.view()
