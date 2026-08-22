def test_hello(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"