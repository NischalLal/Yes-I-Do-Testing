from collections import namedtuple

Task = namedtuple('Task', ['summary','owner','done','id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Use of no parameters should invoke defaults"""
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2

def test_member_access():
    """Check the field functionality of namedtuple"""
    t = Task('Buy a milk', 'Nischal')
    assert t.summary == 'Buy a milk'
    assert t.owner == 'Nischal'
    assert(t.done, t.id) == (False,None)


def test_asdict():
    """_asdit() should return a dictionary"""
    t = Task("Call John", "Nischal", "Yes", 5)
    t = t._asdict()
    expected = {
        'summary':'Call John',
        'owner':'Nischal',
        'done': 'Yes',
        'id':5
    }

    
    assert t == expected


def test_replace():
    """replace"""
    t_before = Task("Finish Book", 'Nischal')
    t_after = t_before._replace(done='Yes',id=5)
    t_expected = Task('Finish Book', 'Nischal', 'Yes', 5)
    assert t_after == t_expected
