from rectangular import rectangular

rec = rectangular(50, 40)
def test_init():
    assert rec.width == 50
    assert rec.height == 40


def test_girth():
    assert rec.girth()==180

def test_area():
    assert rec.area()==2000
