import pytest


def test_hello(capsys):

    from flaskhost.cli import main

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()
    assert "hello" in captured.out
