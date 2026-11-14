from main import Calculator


def test_add():
    cal = Calculator()
    assert cal.add(20, 50) == 70
    
def test_sub():
    cal = Calculator()
    assert cal.sub(50, 20) == 30
    
def test_mul():
    cal = Calculator()
    assert cal.mul(2, 5) == 10
    
def test_div():
    cal = Calculator()
    assert cal.div(40, 20) == 2