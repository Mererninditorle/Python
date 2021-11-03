def del_pos(a,b):
    return a / b

def del_neg(a,b):
    return a / b


def test_answer_pos():
    assert del_pos(9,3) == 3

def test_answer_neg():
    assert del_neg(9,3) == 4