import pytest

from mx_mul import MatrixCalculator

def geninputs(inputs = ('2', '3', '1', '2', '[1 2]', '[5 3]', '[6 7]', '[5]', '[1]')):
    for _ in inputs:
        yield _


def test_inputs(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs()
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    k.main_hub()
    assert k._matrix_A_width == 2
    assert k._matrix_A_height == 3
    assert k._matrix_B_width == 1
    assert k._matrix_B_height == 2


def test_result(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs()
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))
    k.main_hub()
    assert k._result == [[7], [28], [37]]


def test_exit_1(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['a', '3', '1', '2', '[1 2]', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -1


def test_exit_2(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['0', '0', '0', '0', '[1 2]', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -2


def test_exit_3(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['2', '3', '1', '1', '[1 2]', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -3


def test_exit_4(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['2', '3', '1', '2', '[1 a]', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -4


def test_exit_5(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['2', '3', '1', '2', '|1 2|', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -5


def test_exit_6(monkeypatch):
    k = MatrixCalculator()
    GEN = geninputs(['2', '3', '1', '2', '[1 2 3]', '[5 3]', '[6 7]', '[5]', '[1]'])
    monkeypatch.setattr('builtins.input', lambda _: next(GEN))

    with pytest.raises(SystemExit) as e:
        k.main_hub()
    assert e.type == SystemExit
    assert e.value.code == -6




