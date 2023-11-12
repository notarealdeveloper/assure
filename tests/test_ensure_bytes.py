import io
import ensure
import pathlib
import tempfile

def test_ensure_bytes():
    path = tempfile.mktemp()
    with open(path, 'w') as fp:
        fp.write("Hello world\n")

    from_file_rs = ensure.bytes(open(path, 'r'))
    assert isinstance(from_file_rs, bytes)

    from_file_rb = ensure.bytes(open(path, 'rb'))
    assert isinstance(from_file_rb, bytes)

    from_pathlib = ensure.bytes(pathlib.Path(path))
    assert isinstance(from_pathlib, bytes)

    from_path = ensure.bytes(path)
    assert isinstance(from_path, bytes)

    from_string_io = ensure.bytes(io.StringIO(open(path, 'r').read()))
    assert isinstance(from_string_io, bytes)

    from_bytes_io = ensure.bytes(io.BytesIO(open(path, 'rb').read()))
    assert isinstance(from_bytes_io, bytes)

    from_string = ensure.bytes(open(path, 'r').read())
    assert isinstance(from_string, bytes)

    from_bytes = ensure.bytes(open(path, 'rb').read())
    assert isinstance(from_bytes, bytes)

