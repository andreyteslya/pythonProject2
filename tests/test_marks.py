from pytest import mark

@mark.smoke
def test_1():
    assert True

@mark.smoke
def test_2():
    assert True

@mark.smoke
def test_3():
    assert False

@mark.smoke
def test_4():
    assert False


