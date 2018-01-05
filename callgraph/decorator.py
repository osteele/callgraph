from .recorder import CallGraphRecorder


def decorator(fn=None, recorder=None, label_returns=False, graph_attrs=None):
    """A decorator that instruments a function to record calls to it."""
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
