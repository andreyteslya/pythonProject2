from pytest import mark


data = [('hello', 'world'),
         ('hello', ''),
        ('123', 'world')]
ddt = {
    'argnames':'name,description',
    'argvalues':[('hello', 'world'),
         ('hello', ''),
        ('123', 'world')],
    'ids': ['general test', 'no description test', 'test with digits in name']
}

@mark.parametrize(**ddt)
def test_new_testcases( desktop_app_auth, name, description):
    test_name = 'hello'
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)



