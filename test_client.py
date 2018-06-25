# coding=utf-8


def test_ehlo(smtp):
    print(smtp)
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0


def test_noop(smtp):
    print(smtp)
    response, msg = smtp.noop()
    assert response == 250
    assert 0
