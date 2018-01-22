from .recorder import CallGraphRecorder


class CallGraphInstrumentor(object):
    """A context manager that instruments (dynamically decorators) a collection
    of functions in a namespace on entry, and restores their saved values on
    exit."""

    def __init__(self, names, recorder=None, local_ns=None):
        self.recorder = recorder or CallGraphRecorder()
        self._names = names
        self._ns = local_ns or globals()
        self._restore = None

    def __enter__(self):
        ns = self._ns
        fns = {n: ns[n] for n in self._names if ns[n].__call__}
        for name, fn in fns.items():
            ns[name] = self.recorder.wrap(fn)
        self._restore = fns
        return self.recorder

    def __exit__(self, _type, _value, _traceback):
        ns = self._ns
        fns = self._restore
        for name, fn in fns.items():
            ns[name] = fn
