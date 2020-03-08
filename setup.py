from setuptools import setup

setup(
    name="pyprince",
    version="0.5",
    license="MIT",
    url="https://github.com/sufio/python-pyprince",
    description="Prince xml python wrapper for converting HTML to PDF",
    author="Sufio.com",
    author_email="sufio@sufio.com",
    tests_require=["pytest"],
    packages=["pyprince"],
    include_package_data=True,
)
