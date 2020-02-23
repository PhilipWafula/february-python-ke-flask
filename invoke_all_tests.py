import pytest
import sys

if __name__ == '__main__':

    # Argument definitions here https://gist.github.com/kwmiebach/3fd49612ef7a52b5ce3a
    # or (pytest --help)

    r = pytest.main(['-v', '-x', '-s', 'tests'] + sys.argv[1:])
    exit(r)
