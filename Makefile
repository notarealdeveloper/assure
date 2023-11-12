PKG := ensure

all:
	python -m build --sdist

install: all
	pip install dist/*.tar.gz

develop:
	pip install -e .

check:
	pytest tests

uninstall:
	pip uninstall $(PKG)

clean:
	rm -rv dist/ src/*.egg-info
