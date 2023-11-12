import ensure

def test_ensure_plural():
    n = 42
    l = [n]
    assert ensure.singular(l) == n
    assert ensure.singular(n) == n
    assert ensure.plural(n) == l
    assert ensure.plural(l) == l
    assert ensure.plural({n}) == {n}
    assert ensure.plural((n,l)) == (n,l)

