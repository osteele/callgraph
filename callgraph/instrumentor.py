from .recorder import CallGraphRecorder


class CallGraphInstrumentor(object):
    def __init__(self, names, recorder=None, local_ns=None):
        self.recorder = recorder or CallGraphRecorder()
        self._names = names
        self._ns = local_ns or globals()

    def __enter__(self):
        ns = self._ns
        fns = {n: ns[n] for n in self._names if ns[n].__call__}
        for n, fn in fns.items():
            ns[n] = self.recorder.wrap(fn)
        self._restore = fns
        return self.recorder

    def __exit__(self, type, value, traceback):
        ns = self._ns
        fns = self._restore
        for n, fn in fns.items():
            ns[n] = fn
