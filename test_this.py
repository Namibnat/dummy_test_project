import main


def test_this():
    assert 1 == 1


def test_random_number():
    assert main.gen_number() <= 100
    assert main.gen_number() >= 1
