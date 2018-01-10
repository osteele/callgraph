from .recorder import CallGraphRecorder


def decorator(fn=None, recorder=None, label_returns=False, graph_attrs=None):
    """Decorator that wraps a function with instrumentation to record calls to
    it, for use in constructing a call graph.

    Parameters
    ----------
    recorder : CallGraphRecorder, optional
        An CallGraphRecorder. If this is not supplied, a new recorder is created
        with the specified values for ``label_returns`` and ``graph_attrs``,
        and attached to the decorated function as ``fn.__callgraph__``.
    label_returns : bool
        If true, arrows are draw from callee to caller, and labeled with the
        return value.
    graph_attrs : dict
        Graphviz graph attributes. These are passed to
        :meth:`graphviz.Digraph.attr`.
        A new :class:`graphviz.Digraph`.

    Examples
    --------
    ::

        import callgraph.decorator as callgraph

        @callgraph()
        def nchoosek(n, k):
            if k == 0:
                return 1
            if n == k:
                return 1
            return nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)
    """
    rec = recorder or CallGraphRecorder(label_returns=label_returns,
                                        graph_attrs=graph_attrs)

    def graphing_decorator(fn):
        wrapper = rec.wrap(fn)
        if not recorder:
            wrapper.__callgraph__ = rec.graph
        return wrapper
    # The following allows the decorator to be used as either `decorator` or
    # `decorator()`. The examples don't currently demonstrate this, and it
    # may be a bad idea.
    return graphing_decorator(fn) if fn else graphing_decorator
