from .recorder import CallGraphRecorder


def decorator(fn=None, recorder=None, label_returns=False, graph_attrs=None):
    """A decorator that can be used to instrument a function."""
    rec = recorder or CallGraphRecorder(label_returns=label_returns,
                                        graph_attrs=graph_attrs)

    def graphing_decorator(fn):
        wrapper = rec.wrap(fn)
        if not recorder:
            wrapper.__callgraph__ = rec.graph
        return wrapper
    return graphing_decorator(fn) if fn else graphing_decorator
