import sys

from .ze2nb import ze2nb


if __name__ == "__main__":
    filename = sys.argv[1]
    ze2nb(filename)
