from collections import namedtuple

Task = namedtuple('Task', ['summary' 'owner' 'done','id'])
Task.__new__.__defaults__=(None,None,False,None)


def test_defaults():
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2