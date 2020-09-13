import os
from contextlib import contextmanager
from typing import ContextManager, Union


@contextmanager
def atomic_write(
    file: Union[str, os.PathLike], mode: str = "w", as_file: bool = True, **kwargs
) -> ContextManager:
    """Write a file atomically

    :param file: str or :class:`os.PathLike` target to write
    :param mode: the mode in which the file is opened, defaults to "w" (writing in text mode)
    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string

    :param kwargs: anything else needed to open the file

    :raises: FileExistsError if target exists

    Example::

        with atomic_write("hello.txt") as f:
            f.write("world!")

    """
    raise NotImplementedError()
