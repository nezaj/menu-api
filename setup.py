from setuptools import setup, find_packages

# hack to fix a Python 2.7.3 issue with multiprocessing module --
# see http://bugs.python.org/issue15881
# pylint:disable=unused-import
try:
    import multiprocessing
except ImportError:
    pass

dependencies = [
    # Tornado
    "tornado==4.2.1",
    # Static analysis
    "pep8>=1.6.2",
    "pylint>=1.4.4",
    # Testing
    "pytest==2.8.2",
    "pytest-tornado==0.4.4"
]

setup(
    name="tornado-menu-api",
    version="0.1",
    packages=find_packages(),
    zip_safe=False,
    install_requires=dependencies
)
