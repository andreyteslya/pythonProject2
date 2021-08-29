def test_new_alice1(desktop_app_auth):
    test_name = 'hello'
    desktop_app_auth.navigate_to('Create_new_test')
    desktop_app_auth.create_test(test_name, 'world')
    desktop_app_auth.navigate_to('Test cases')
    assert desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)


