try:
    from pyflicka import service as _main
except ImportError:
    from flicka import service as _main

if __name__ == "__main__":
    _main()
