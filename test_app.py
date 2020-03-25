import lib


def patched():
    return b'2'


def test_test(app, monkeypatch):
    monkeypatch.setattr(lib, "foo", patched)
    result = app.get('/')
    assert result.data == b"2"
