# Execute the examples. This is a quick manual sanity check for errors.
#
# The decorator-examples test could be turned into an automated test case.
#
# The magic-examples notebook contains gratuitous differences when it's
# re-executed, since the notebook contains the repr of the Graphviz Diagraph
# instances, which include their addresses. Testing for the decorator should
# inspect the digraph or compare its generated dot or SVG file, rather than
# using the notebook.
.PHONY: execute
execute:
	jupyter nbconvert --to notebook --execute examples/callgraph-decorator-examples.ipynb --inplace --ExecutePreprocessor.kernel_name=python
	jupyter nbconvert --to notebook --execute examples/callgraph-magic-examples.ipynb --inplace --ExecutePreprocessor.kernel_name=python
