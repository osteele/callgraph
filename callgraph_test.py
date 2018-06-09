import os
import subprocess
import nbformat

from pathlib import Path

PROJECT_HOME = Path(os.path.dirname(__file__))
EXAMPLE_NB_PATH = PROJECT_HOME / 'examples/callgraph-magic-examples.ipynb'
IPYTHON_CONFIG_PATH = PROJECT_HOME / 'config/ipython_config.py'


def read_notebook(basename):
    "Read notebook `basename` from the test files directory."
    if not basename.endswith('.ipynb'):
        basename += '.ipynb'
    return nbformat.read(
        os.path.join(os.path.dirname(__file__), 'files', basename),
        as_version=4)


def test_callgraph():
    res = subprocess.run(["jupyter", "nbconvert",
               "--to", "notebook",
               "--config=" + str(IPYTHON_CONFIG_PATH),
               "--execute", str(EXAMPLE_NB_PATH),
               "--ExecutePreprocessor.kernel_name=python3",
               "--stdout",
               ],
              stdout=subprocess.PIPE)
    assert res.returncode == 0
    assert res.stdout is not None
    gm = read_notebook(str(EXAMPLE_NB_PATH))
    nb = nbformat.reads(res.stdout, as_version=4)
    assert nb == gm
