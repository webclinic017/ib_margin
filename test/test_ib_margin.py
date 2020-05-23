from pathlib import Path

from ib_margin.ib_margin import download, merge, read, write


def test_module() -> None:

    # read existing margin file and merge with downloaded margin
    path = Path("test/test_data.csv")
    old = read(path)
    new = download()
    result = merge(old, new.head(10))
    write(result, path)
