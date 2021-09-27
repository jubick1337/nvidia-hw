pretty:
	black . -l 120 -t py38
	isort . -l 120 --skip-gitignore --lines-between-types 1
	autoflake . --in-place --remove-unused-variables -r


lint:
	mypy **/*.py --no-namespace-packages
	flake8 . --max-line-length 120
	pylint . --exit-zero