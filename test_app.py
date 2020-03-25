import lib


def patched():
    return b'2'


def test_test(app, monkeypatch):
    result = app.get('/')

    monkeypatch.setattr(lib, "foo", patched)

    assert result.data == b"2"
