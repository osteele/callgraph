.PHONY: execute
execute:
	jupyter nbconvert --to notebook --execute examples/callgraph-decorator-examples.ipynb --inplace --ExecutePreprocessor.kernel_name=python
	jupyter nbconvert --to notebook --execute examples/callgraph-magic-examples.ipynb --inplace --ExecutePreprocessor.kernel_name=python
