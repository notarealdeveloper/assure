PKG := ensure

all:
	python -m build --sdist

install: all
	pip install dist/*.tar.gz

uninstall:
	pip uninstall $(PKG)

clean:
	rm -rv dist/ src/*.egg-info
