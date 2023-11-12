import os
import sys
import ensure

def make_stream(mode):
    return os.fdopen(os.popen("echo hello world").fileno(), mode)

def test_ensure_stream():
    stream = make_stream('r')
    assert not stream.seekable()
    assert ensure.seekable(stream).seekable()

    stream = make_stream('rb')
    assert not stream.seekable()
    assert ensure.seekable(stream).seekable()

