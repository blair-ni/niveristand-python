import inspect


def test_validate(testmodule):
    funcs = [n for n, f in inspect.getmembers(testmodule, inspect.isfunction) if
             not (n.startswith('test') or n.startswith('idfunc') or n.startswith('_'))]
    lists = [testmodule.__dict__.get(a) for a in dir(testmodule)
             if a.startswith('run_tests') or a.startswith('skip_tests') or
             a.startswith('transform_tests') or a.startswith('fail_transform_tests')]
    final_list = []
    for list in lists:
        for item in list:
            final_list.append(item[0].__name__)
    not_assigned = [f for f in funcs if f not in final_list]
    assert not_assigned == [], "Test " + not_assigned.__str__() + " in " + testmodule.__name__ \
                               + " is not added to any list."
