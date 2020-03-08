.PHONY: sdist wheel upload clean

release: sdist wheel upload

sdist:
	python setup.py sdist

wheel:
	python setup.py bdist_wheel

upload:
	python setup.py sdist upload -r sufiopypi
	python setup.py bdist_wheel upload -r sufiopypi

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .tox
